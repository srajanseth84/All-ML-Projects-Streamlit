import streamlit as st
from FTG import ftg
from Text_Generator import txt_generator
from Food_Vision import food_vision
from Neural_Style_Transfer import neural_style_transfer
from Sentiment_Classification import sentiment_classification


PAGES = {
    "Fill the Gap": ftg,
    "Text Generator Using GPT-2": txt_generator,
    "Food Vision": food_vision,
    "Neural Style Transfer": neural_style_transfer,
    "Sentiment Classification": sentiment_classification
}

st.sidebar.title('Select Project')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES.get(selection)
page.app()
