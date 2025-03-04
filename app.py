import streamlit as st
import plotly.express as px

# App Title
st.title("🤖 BMI Tracker and Health Advisor")

# User Input
weight = st.number_input("Enter your weight (in kgs)")
height = st.number_input("Enter your height (in meters)")

# Function to give Health Advice
def get_health_advice(bmi):
    if bmi < 18.5:
        return "🔹 You are **Underweight**. Try to eat a balanced diet and gain healthy weight."
    elif 18.5 <= bmi < 24.9:
        return "✅ You have a **Normal Weight**. Keep maintaining a healthy lifestyle!"
    elif 25 <= bmi < 29.9:
        return "⚠️ You are **Overweight**. Consider a healthy diet and exercise routine."
    else:
        return "🚨 You are **Obese**. Consult a doctor and focus on weight management."

# Calculate BMI
bmi = None
if height > 0 and weight > 0:
    bmi = round(weight / (height ** 2), 2)
    st.success(f"Your BMI Index is {bmi}")
    
    # Show Health Advice
    advice = get_health_advice(bmi)
    st.warning(advice)  # Warning box for advice

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
