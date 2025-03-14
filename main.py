import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place:")
forecast_days = st.slider(label="Forecast Days:",
                          min_value=1,
                          max_value=5,
                          help="Select the number of forecasted days")
options = st.selectbox(label="Select data to view:",
                       options=('Temperature', 'Sky'))
st.subheader(f"{options} for the next {forecast_days} {"day" if forecast_days == 1 else "days"} in {place}: ")

def get_data(forecast_days):
    dates = ["2022-01-10", "2022-02-10", "2022-03-10"]
    temperatures = [17, 48, 39]
    temperatures = [forecast_days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(forecast_days)

figure = px.line(x=d,
                 y=t,
                 labels={"x": "Date", "y": "Temperatures (°C)"})
st.plotly_chart(figure)