import streamlit as st
import requests
import time

def app():

    st.title("Know the Sentiment🧐")
    st.write("To know more about this app, visit [**GitHub**](https://github.com/srajanseth84/Sentiment-Classification)")

    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer " + str(st.secrets["sentiment_api_token"])}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    st.write("### Enter Sentence")
    input = st.text_input(" ")
    button = st.button("Find out🧐")

    if button and not input:
        st.warning("⚠️ Please INPUT a Sentence ⚠️")

    try:
        with st.spinner("Classifying Sentiment"):
            if button and input:
                output = query({"inputs": input})
                for sentence in output:
                    for pred in sentence:
                        col1 , col2 = st.columns(2)
                        with col1:
                            label_score = pred["label"] +"      " + str(format(pred["score"]*100,".2f")) + "%"
                            symbol = ""
                            if pred["label"] == "NEGATIVE":
                                symbol = "    👎"
                            else:
                                symbol = "    👍"
                            if pred["score"] > 0.5:
                                st.success(label_score + symbol)
                            else:
                                st.write(label_score)
                        with col2:
                            my_bar = st.progress(0)
                            for percent_complete in range(int(pred["score"]*100)):
                                time.sleep(0.01)
                                my_bar.progress(percent_complete + 1)
    except:
        st.warning("Some **Unexpected** Error happen")
        st.warning("Please create a **Issue** on [Github](https://github.com/srajanseth84/Sentiment-Classification)")


    st.markdown("Created by **Srajan Seth**")
    st.markdown(body="""
    <th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
    <th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>
    """, unsafe_allow_html=True)