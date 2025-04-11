import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
import json

FILE_PATH = "attendance.txt"
st.set_page_config(page_title="🕒 Attendance System", layout="wide")

def load_data():
    required_columns = ['Date', 'Entry', 'Exit', 'Break', 'Extra', 'Total']
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
            if not data:
                return pd.DataFrame(columns=required_columns)
            df = pd.DataFrame(data)
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)
            df = df.dropna(subset=['Date'])
            return df
        except Exception as e:
            return pd.DataFrame(columns=required_columns)
    return pd.DataFrame(columns=required_columns)

def save_data(df):
    try:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        data = df.to_dict(orient='records')
        with open(FILE_PATH, "w") as f:
            json.dump(data, f)
    except Exception as e:
        st.error(f"Error saving data: {e}")

st.markdown("""
    <style>
    body, .stApp { background-color: #F5DEB3; color: #333333; }
    .stButton>button { background-color: black important; border-radius: 8px; }
    .stButton>button:hover { background-color: #000000 important; }
    .title { font-size: 28px; font-weight: bold; text-align: center; color: #000; }
    .warning-box { background-color: #ffcccc; padding: 10px; border-radius: 8px; text-align: center; }
    .info-box { background-color: #cce5ff; padding: 10px; border-radius: 8px; text-align: center; }
    .header { font-size: 22px; font-weight: bold; color: #000; }
    .custom-label { font-size: 18px; font-weight: bold; padding-bottom: 5px; }
    .blue { color: #0044cc; }
    .green { color: #008000; }
    .red { color: #cc0000; }
    .purple { color: #800080; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🕒 Attendance Management System</div>', unsafe_allow_html=True)

with st.form("entry_form"):
    cols = st.columns(4)

    with cols[0]:
        st.markdown('<div class="custom-label blue">📅 Select Date</div>', unsafe_allow_html=True)
        date = st.date_input(" ", datetime.today(), key="date", label_visibility="collapsed")

    with cols[1]:
        st.markdown('<div class="custom-label green">🚪 Entry Time</div>', unsafe_allow_html=True)
        entry_time = st.time_input(" ", key="entry_time", label_visibility="collapsed")

    with cols[2]:
        st.markdown('<div class="custom-label red">🏁 Exit Time</div>', unsafe_allow_html=True)
        exit_time = st.time_input(" ", key="exit_time", label_visibility="collapsed")

    with cols[3]:
        st.markdown('<div class="custom-label purple">☕ Break Time (Hours)</div>', unsafe_allow_html=True)
        break_time = st.number_input(" ", min_value=0.0, step=0.5, key="break_time", label_visibility="collapsed")

        st.markdown('<div class="custom-label purple">⏳ Overtime (Hours)</div>', unsafe_allow_html=True)
        extra_time = st.number_input(" ", min_value=0.0, step=0.5, key="extra_time", label_visibility="collapsed")

    if st.form_submit_button("✅ Submit"):
        entry_dt = datetime.combine(date, entry_time)
        exit_dt = datetime.combine(date, exit_time)
        if exit_dt < entry_dt:
            exit_dt += timedelta(days=1)
        total_hours = max(0, (exit_dt - entry_dt).total_seconds() / 3600 - break_time + extra_time)
        new_entry = pd.DataFrame([{
            'Date': date,
            'Entry': entry_time.strftime("%H:%M"),
            'Exit': exit_time.strftime("%H:%M"),
            'Break': break_time,
            'Extra': extra_time,
            'Total': total_hours
        }])
        if not new_entry.isna().all().all():
            df = pd.concat([load_data(), new_entry], ignore_index=True)
            save_data(df)
            st.success("✅ Data saved successfully!")
        else:
            st.warning("⚠️ The entry data is empty.")

df = load_data()
date_range = df['Date'].dt.date.unique() if not df.empty else []

with st.sidebar:
    st.markdown('<div class="header green">🔍 Filters</div>', unsafe_allow_html=True)
    start_date = st.date_input("From", min(date_range) if len(date_range) > 0 else datetime.today())
    end_date = st.date_input("To", max(date_range) if len(date_range) > 0 else datetime.today())

if not df.empty:
    filtered = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)]
    display_df = filtered.copy()
    display_df['Date'] = display_df['Date'].dt.date
else:
    display_df = pd.DataFrame()

st.markdown('<div class="header">📜 Attendance Records</div>', unsafe_allow_html=True)
if not display_df.empty:
    st.dataframe(display_df, use_container_width=True)
else:
    st.markdown('<div class="warning-box">⚠️ No records found.</div>', unsafe_allow_html=True)

st.markdown('<div class="header">📊 Work Hours per Day</div>', unsafe_allow_html=True)
if not display_df.empty:
    display_df['Date'] = pd.to_datetime(display_df['Date'])
    daily_work_hours = display_df.groupby('Date')['Total'].sum().reset_index()
    st.line_chart(daily_work_hours, x='Date', y='Total')
    st.dataframe(daily_work_hours, use_container_width=True)
    total_work_hours = daily_work_hours['Total'].sum()
    st.markdown(f'<div class="info-box">Total work hours: {total_work_hours:.2f} hours</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="info-box">ℹ️ No data available</div>', unsafe_allow_html=True)
