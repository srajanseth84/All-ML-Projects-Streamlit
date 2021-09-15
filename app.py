import streamlit as st
from FTG import ftg
from Text_Generator import txt_generator
from Food_Vision import food_vision
from Neural_Style_Transfer import neural_style_transfer
from Sentiment_Classification import sentiment_classification

st.set_page_config(page_title="Srajan's ML Projects",
                   page_icon="👨‍💻")


PAGES = {
    "Food Vision 🍕📷": food_vision,
    "Text Generator 📜": txt_generator,
    "Neural Style Transfer 🖼": neural_style_transfer,
    "Fill the Gap 💡": ftg,
    "Sentiment Classification 🧐": sentiment_classification
}

st.sidebar.title(' Select Project 🗂')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
for i in range(25):
    st.sidebar.markdown("\n")
st.sidebar.markdown("Created by **Srajan Seth**")
st.sidebar.markdown(body="""
<th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
<th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>
""", unsafe_allow_html=True)
page = PAGES.get(selection)
page.app()

