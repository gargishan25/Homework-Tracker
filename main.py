import streamlit as st
import pandas as pd
datatable = pd.DataFrame()
# Create page
st.set_page_config(page_title = "Homework Tracker", page_icon = "📚")
st.title("Homework Tracker")
# Save previous submissions
if "tasks" not in st.session_state:
    st.session_state.tasks = []

assignment = st.text_area("Assignment Name: ")
subject = st.text_area("Class Name: ")
due = st.date_input("Due Date: ")
# Ensure that the user has inputed something, adding information to list.
if st.button("Add to Task List"):
    if assignment.strip() == "" or subject.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.session_state.tasks.append({"Assignment" : assignment, "Subject" : subject, "Due Date" : due})
        st.write("Task Added")

# Show the final table.
if st.button("Show Task List"):
    st.subheader("Homework To Do In Order")
    datatable = pd.DataFrame(st.session_state.tasks)
    # st.write(datatable)
    datatable = datatable.sort_values("Due Date") # Sort the table
    st.dataframe(datatable)