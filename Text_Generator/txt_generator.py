import streamlit as st
from transformers import pipeline

def app():
    @st.cache(allow_output_mutation=True)
    def load_model():
        generator = pipeline('text-generation', model='gpt2')
        return generator

    def generate_text(gererator, raw_text, max_length, num_return_sequences):
        return generator(raw_text, max_length=max_length, num_return_sequences=num_return_sequences)

    st.title("Text Generation 📜")
    st.write('**Looking for Words? Use TEXT GENERATOR😉**\n')
    st.write(
        "To know more about this app, visit [**GitHub**](https://github.com/srajanseth84/Text-Generator-using-GPT2)")

    model_state = st.text("Loading model")
    generator = load_model()
    model_state.text("Loading model done")

    st.subheader("Generate Text")
    st.write("### Enter Text Here")
    raw_text = st.text_area(' ', height=25)
    st.markdown("### Select Max-Length of Each Sentence")
    max_length = st.slider('More Length = More Time', min_value=50, max_value=150)
    st.markdown("### Number of Sequences")
    num_return_sequences = st.selectbox(
        "More Sequence = More Time", [2, 3, 4, 5, 6, 7])

    button = st.button("Generate 📜")

    if button and not input:
        st.warning("⚠️ Please INPUT a Sentence ⚠️")

    try:
        with st.spinner("Generating Text"):
            if button and input:
                output = generate_text(generator, raw_text,
                                       max_length, num_return_sequences)
                i = 1
                for sentence in output:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("### Generated Text " + str(i) + ":")
                    with col2:
                        st.write(sentence["generated_text"])
                    i = i + 1
                    st.markdown("---")


    except:
        st.warning("Some **Unexpected** Error happen")
        st.warning(
            "Please create a **Issue** on [Github](https://github.com/srajanseth84/Text-Generator-using-GPT2)")

    st.markdown("Created by **Srajan Seth**")
    st.markdown(body="""
    <th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
    <th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>
    """, unsafe_allow_html=True)
