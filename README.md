# **Attendance Tracker Pro**  
**📊 Employee Work Hours Management System**  


## **Repository Name**  
`attendance-tracker-pro`  

---

## **📌 Overview**  
A Streamlit-based **employee attendance tracking system** with:  
- 🕒 **Time logging** (entry/exit/breaks)  
- 📈 **Interactive work hours visualization**  
- 📅 **Date filtering** and analytics  
- 💾 **Persistent JSON data storage**  

Perfect for small businesses and teams needing simple yet powerful attendance monitoring.

---

## **✨ Key Features**  

### **📝 Time Tracking**  
- Entry/Exit time recording  
- Break time deduction  
- Overtime calculation  
- Automatic total hours computation  

### **📊 Data Visualization**  
- **Line chart** of daily work hours  
- Filterable date ranges  
- Total hours summary  

### **🔒 Data Management**  
- JSON storage (easy backup/restore)  
- Table editing capabilities  
- Responsive design  

---

## **🛠️ How to Run**  

### **Prerequisites**  
- Python 3.8+  
- Required packages:  
  ```bash
  pip install streamlit pandas
  ```

### **Launch the App**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yarahmadi0077/attendance-tracker-pro.git
   cd attendance-tracker-pro
   ```

2. Run the application:  
   ```bash
   streamlit run workcalculator.py
   ```

3. Access in browser at:  
   `http://localhost:8501`

---

## **📋 Usage Guide**  

1. **Log Daily Attendance**:  
   - Select date and entry/exit times  
   - Add break duration and overtime  

2. **View Records**:  
   - Filter by date range in sidebar  
   - See all entries in sortable table  

3. **Analyze Trends**:  
   - Interactive line chart shows daily totals  
   - Summary displays cumulative hours  

---

## **⚙️ Technical Details**  
- **Frontend**: Streamlit  
- **Data Storage**: JSON (attendance.txt)  
- **Visualization**: Pandas + Streamlit charts  
- **Error Handling**: Automatic data validation  

---

## **📂 File Structure**  
```
attendance-tracker-pro/
├── workcalculator.py                # Main application
├── attendance.txt        # JSON data storage
├── README.md             # This document
└── requirements.txt      # Dependencies
```

---

## **📜 License**  
MIT License - Free for commercial and personal use  

---
![Screenshot 2025-04-11 152816](https://github.com/user-attachments/assets/aab9000e-fd59-4d2c-987a-f48a36d29b1f)
![Screenshot 2025-04-11 152831](https://github.com/user-attachments/assets/4195f06a-d509-4b00-91de-0abcd66b1ab8)

