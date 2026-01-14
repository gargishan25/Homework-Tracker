import streamlit as st
import pandas as pd
datatable = pd.DataFrame()
st.set_page_config(page_title = "Homework Tracker", page_icon = "📚")
st.title("Homework Tracker")

if "history" not in st.session_state:
    st.session_state.history = []

assignment = st.text_area("Assignment Name: ")
subject = st.text_area("Class Name: ")
due = st.text_area("Due Date (Day/Month/Year): ")
if st.button("Add to Task List"):
    if assignment.strip() == "" or subject.strip() == "" or due.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.session_state.history.append({"Assignment" : assignment, "Subject" : subject, "Due Date" : due})

# st.write(tasks)
if st.button("Show Task List"):
    st.subheader("Homework To Do In Order")
    datatable = pd.DataFrame(st.session_state.history)
    st.dataframe(datatable)