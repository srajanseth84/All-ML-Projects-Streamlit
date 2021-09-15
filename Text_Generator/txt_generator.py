import streamlit as st
from transformers import pipeline

def app():
    @st.cache(allow_output_mutation=True)
    def load_model():
        generator = pipeline('text-generation', model='gpt2')
        return generator


    def generate_text(gererator, raw_text):
        return generator(raw_text, max_length=50, num_return_sequences=5)


    st.title("Text Generation")

    model_state = st.text("Loading model")
    generator = load_model()
    model_state.text("Loading model done")


    st.subheader("Generate Text")
    raw_text = st.text_area("Enter Text Here", height=25)

    if st.button("Generate"):
        output = generate_text(generator, raw_text)
        st.write(output)

    st.markdown("Created by **Srajan Seth**")
    st.markdown(body="""
    <th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
    <th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>
    """, unsafe_allow_html=True)
