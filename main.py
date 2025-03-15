import streamlit as st
import plotly.express as px
from backend import get_data

# Front-end i.e. (Adding title, text input, slider, selectbox and subheader):
st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:")
forecast_days = st.slider(label="Forecast Days:",
                          min_value=1,
                          max_value=5,
                          help="Select the number of forecasted days")
options = st.selectbox(label="Select data to view:",
                       options=('Temperature', 'Sky'))
st.subheader(f"{options} for the next {forecast_days} {"day" if forecast_days == 1 else "days"} in {place}: ")


if place:
    try:
        # Backend i.e. (Get the temperature/sky data)
        filtered_data = get_data(place, forecast_days)

        if options == "Temperature":
            kelvin_temperatures = [key["main"]["temp"] for key in filtered_data]
            kelvin_to_celsius = [(temp - 273.15) for temp in kelvin_temperatures]
            dates = [date["dt_txt"] for date in filtered_data]

            # Create a temperature plot
            figure = px.line(x=dates,
                             y=kelvin_to_celsius,
                             labels={"x": "Date", "y": "Temperatures (°C)"})
            st.plotly_chart(figure)


        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [key["weather"][0]['main'] for key in filtered_data]
            times = [time["dt_txt"] for time in filtered_data]
            images_paths = [images[condition] for condition in sky_condition]
            # Create a Sky figure
            st.image(images_paths, width=150, caption=times)

    except KeyError:
        st.info(f"{place} doesn't exist. Please try again!")