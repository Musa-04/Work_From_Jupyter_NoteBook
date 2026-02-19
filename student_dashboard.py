import streamlit as st
import pandas as pd
import os

FILE_NAME = "students.csv"

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    return pd.DataFrame(
        columns=["Name", "Subject1", "Subject2", "Subject3", "Average", "Grade"]
    )

def save_data(df):
    df.to_csv(FILE_NAME, index=False)

st.set_page_config(page_title="Student Dashboard", layout="centered")
st.title("🎓 Student Dashboard")

menu = st.sidebar.radio("Menu", ["Add Student", "View Students"])

if menu == "Add Student":
    st.subheader("➕ Add Student")

    name = st.text_input("Student Name")

    col1, col2, col3 = st.columns(3)
    with col1:
        m1 = st.number_input("Subject 1", 0, 100)
    with col2:
        m2 = st.number_input("Subject 2", 0, 100)
    with col3:
        m3 = st.number_input("Subject 3", 0, 100)

    if st.button("Save"):
        if name.strip() == "":
            st.error("Name cannot be empty")
        else:
            avg = round((m1 + m2 + m3) / 3, 2)
            grade = calculate_grade(avg)

            df = load_data()
            df.loc[len(df)] = [name, m1, m2, m3, avg, grade]
            save_data(df)

            st.success(f"Saved! Grade: {grade}")

else:
    st.subheader("📊 Student Records")
    df = load_data()

    if df.empty:
        st.warning("No records found")
    else:
        st.dataframe(df)
        st.metric("Total Students", len(df))
        st.metric("Class Average", round(df["Average"].mean(), 2))
