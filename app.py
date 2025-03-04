import streamlit as st
import plotly.express as px

# App Title
st.title("🤖 BMI Tracker and Health Advisor")

# User Input
weight = st.number_input("Enter your weight (in kgs)")
height = st.number_input("Enter your height (in meters)")

# Calculate BMI
bmi = None
if height > 0 and weight > 0:
    bmi = round(weight / (height ** 2), 2)
    st.success(f"Your BMI Index is {bmi}")

# BMI History store in session_state
if 'bmi_history' not in st.session_state:
    st.session_state.bmi_history = []

if bmi is not None:
    st.session_state.bmi_history.append(bmi)

# Show BMI History with Plotly
st.subheader("📊 BMI Progress Chart")

if len(st.session_state.bmi_history) > 1:
    fig = px.line(x=list(range(1, len(st.session_state.bmi_history) + 1)), 
                  y=st.session_state.bmi_history, 
                  markers=True,
                  title="Your BMI Trend",
                  labels={'x': "Record Number", 'y': "BMI Value"})
    
    st.plotly_chart(fig)
else:
    st.info("Add more records to see the trend.")
