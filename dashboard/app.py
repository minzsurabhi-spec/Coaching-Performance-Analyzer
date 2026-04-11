import streamlit as st
import pandas as pd


# Loading  dataset -------------------------------------------------------
df = pd.read_csv("data/coaching_student_final.csv")

st.title("📊 Student Performance Dashboard")

st.write("### Student Data")
st.dataframe(df)

#Adding search feature ----------------------------------------------------

student_name = st.text_input("Search Student by Name")

if student_name:
    df = df[df["Name"].str.contains(student_name, case=False)]

#Showing columns

st.dataframe(df[[
    "Name",
    "Category",
    "Strong Subjects",
    "Weak Subjects",
    "Recommendation"
]])


#sidebar filters -------------------------------------------------------

st.sidebar.header("Filters")

category_filter = st.sidebar.selectbox(
    "Select Category",
    ["All", "Strong", "Average", "Weak"]
)

if category_filter != "All":
    df = df[df["Category"] == category_filter]


#Charts -------------------------------------------------------

st.write("### Category Distribution")

st.bar_chart(df["Category"].value_counts()) 

st.write("### Students Needing Attention")

weak_students = df[df["Category"] == "Weak"]

st.dataframe(weak_students)