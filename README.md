# 📊 Coaching Performance Analyzer

## 📌 Project Overview

The **Coaching Performance Analyzer** is a data analytics project built using Python that helps teachers to analyze student performance .
It processes student marks, identifies strengths and weaknesses, and provides personalized recommendations along with teacher-level insights.

---

## 🎯 Objectives

* Analyze student performance based on subject-wise marks
* Classify students into performance categories
* Identify weak and strong subjects
* Provide personalized recommendations
* Help teachers make data-driven decisions

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** – Data manipulation & analysis
* **Matplotlib / Seaborn** – Data visualization
* **Streamlit** – Interactive dashboard

---

## 📂 Project Structure

```
Coaching-Performance-Analyzer/
│
├── data/
│   ├── coaching_student_data.csv
│   └── coaching_student_final.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── classification.py
│   └── recommendation.py
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Features

### 📊 Data Processing

* Cleaned and structured real student data
* Calculated Total Marks and Percentage
* Assigned Grades

---

### 🧠 Student Analysis

* Classified students into:

  * Strong
  * Average
  * Weak
* Identified:

  * Weak subjects (marks < 40)
  * Strong subjects (marks ≥ 75)

---

### ⭐ Recommendation System

* Generates personalized feedback for each student
* Suggests areas of improvement
* Highlights strong performance

---

### 👨‍🏫 Teacher Insights

* Identifies hardest subject (lowest average score)
* Detects students needing extra attention
* Provides class performance summary

---

### 💻 Interactive Dashboard

Built using Streamlit with features:

* 🔍 Search student by name
* 📊 Category filtering
* 📈 Performance charts
* 📌 Detailed student analysis
* 📥 Download report option
* 🧠 Smart insights

---

## ▶️ How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/your-username/coaching-performance-analyzer.git
cd coaching-performance-analyzer
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run Streamlit App

```
streamlit run dashboard/app.py
```

---

## 📊 Some Insights

* Students are weakest in a particular subject based on average scores
* Identification of top students
* Personalized recommendations for each student

---

## 🚀 Future Improvements

* Integration with database
* Real-time data updates
* Machine learning model for performance prediction
* Multi-class comparison

---

## 📌 Author
  Surabhi Minz 
---

## 💡 Key Learning

This project demonstrates how raw data can be transformed into meaningful insights and used to support real-world decision-making in an educational environment.
