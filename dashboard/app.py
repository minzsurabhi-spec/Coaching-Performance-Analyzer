import streamlit as st
import pandas as pd


# Loading  dataset -------------------------------------------------------
df = pd.read_csv("data/coaching_student_final.csv")

# Dashboard Title --------------------------------------------------------------------------------------------------------------
st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
📊 Coaching Performance Analyzer
</h1>
""", unsafe_allow_html=True)

st.write("### Student Data")
st.dataframe(df)


# Show top students----------------------------------------------------------------------------------------------------------------
st.subheader("🏆 Top 5 Students")
top_students = df.sort_values(by="Percentage", ascending=False).head(5)
top_students['Recommendation'] = top_students.apply(
    lambda row: f"Outstanding performance! Keep it up 🚀",
    axis=1
)
st.dataframe(top_students)


# Show weak students---------------------------------------------------------------------------------------------------------------
st.subheader("⚠️ Weak Students")
weak_students = df[df["Percentage"] < 50]

if weak_students.empty:
    st.write("No weak students 🎉")
else:
    st.dataframe(weak_students)



st.divider()





#Adding search feature -----------------------------------------------------

student_name = st.text_input("Search Student by Name")

filtered_df = df.copy()

if student_name:
    filtered_df = df[df["Name"].str.contains(student_name, case=False)]

if filtered_df.empty:
    st.warning("No student found")


#Selected student details----------------------------------------------------------------------------------------------------------------

if student_name and not filtered_df.empty:
    
    st.subheader("🎯 Student Detailed Analysis")
    
    student = filtered_df.iloc[0]   # first matched student
    
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📌 Basic Info")
        st.write(f"**Name:** {student['Name']}")
        st.write(f"**Category:** {student['Category']}")
        st.write(f"**Percentage:** {round(student['Percentage'], 2)}")

    with col2:
        st.write("### 📊 Subjects")
        st.write(f"**Strong Subjects:** {student['Strong Subjects']}")
        st.write(f"**Weak Subjects:** {student['Weak Subjects']}")


#Recommendations----------------------------------------------------------------------------------------------------------------

    st.subheader("📌 Recommendation")
    st.success(student["Recommendation"])



#Charts -------------------------------------------------------

st.write("### Category Distribution")

st.bar_chart(df["Category"].value_counts()) 



#Subject wise performance chart----------------------------------------------------------------------------------------------------------------

if student_name and not filtered_df.empty:
    student = filtered_df.iloc[0]  

    import matplotlib.pyplot as plt

    subjects = ["English", "Hindi", "Maths", "Science", "Social Science", "Computer"]
    marks = [student[sub] for sub in subjects]

    fig, ax = plt.subplots()
    ax.bar(subjects, marks)

    ax.set_title("Subject-wise Performance")
    plt.xticks(rotation=45)

    st.pyplot(fig)

#Students Insights-----------------------------------------------------------------------------------------------------------------------


st.subheader("🧠 Insights")

# Hardest subject
subject_avg = df[["English", "Hindi", "Maths", "Science", "Social Science", "Computer"]].mean()
hardest_subject = subject_avg.idxmin()

st.warning(f"📌 Students are weakest in {hardest_subject}")

# Weak students count
weak_count = len(df[df["Category"] == "Weak"])

st.error(f"⚠️ {weak_count} students need serious attention")



#Metrics-----------------------------------------------------------------------------------------------------------------------

st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Average %", round(df["Percentage"].mean(), 2))
col3.metric("Top Score", df["Percentage"].max())