import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place:")
forecast_days = st.slider(label="Forecast Days:", min_value=1, max_value=5, help="Select the number of forecasted days")
options = st.selectbox(label="Select data to view:", options=('Temperature', 'Sky'))
st.subheader(f"{options} for the next {forecast_days} {"day" if forecast_days == 1 else "days"} in {place}: ")