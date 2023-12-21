import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style


st.title('🚢 Titanic - Animated Chart')
st.markdown("<h6>Titanic, launched on May 31, 1911, and set sail on its maiden voyage from Southampton on April 10, 1912, with 2,240 passengers and crew on board. On April 15, 1912, after striking an iceberg, Titanic broke apart and sank to the bottom of the ocean, taking with it the lives of more than 1,500 passengers and crew.</h6)", unsafe_allow_html=True)


def create_chart():

    # initialize chart
    chart = Chart(width="640px", height="360px", display="manual")

    # add data
    data = Data()
    data_frame = pd.read_csv("https://ipyvizzu.vizzuhq.com/0.16/showcases/titanic/titanic.csv")
    data.add_df(data_frame)

    chart.animate(data)

    # add config
    chart.animate(Config({"x": "Count", "y": "Sex", "label": "Count","title":"Passengers of the Titanic*"}))
    chart.animate(Config({"x": ["Count","Survived"], "label": ["Count","Survived"], "color": "Survived"}))
    chart.animate(Config({"x": "Count", "y": ["Sex","Survived"]}))
    chart.animate(Config({"x": "Count", "y": ["Sex", "Survived"]}))
    chart.animate(Config({"x": ["Count", "Sex", "Survived"],"y": None, "coordSystem": "polar",}))


    # add style
    chart.animate(Style({"title": {"fontSize": 20}}))

    return chart._repr_html_()


def refresh_page():
    st.markdown('<script>location.reload();</script>', unsafe_allow_html=True)


CHART = create_chart()
html(CHART, width=650, height=370)

st.write("*Dataset contains similar information but does not disclose the “ground truth” for each passenger.")

refresh_button = st.button('Refresh Chart')

if refresh_button:
    refresh_page()

    st.write("Teste")
