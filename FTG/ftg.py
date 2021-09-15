import streamlit as st
from transformers import pipeline
from transformers.pipelines import PipelineException

def app():

    # st.set_page_config(page_title="Fill the GAP",
    #                    page_icon="💡")

    st.title("Fill the GAP💡")
    st.write("Replace ``_`` with ``[MASK]`` ")
    st.write("Ex: The Air of ``_`` is very fresh. ``-->`` The Air of ``[MASK]`` is very fresh.")
    st.write("To know more about this app, visit [**GitHub**](https://github.com/srajanseth84/FTG)")

    @st.cache(allow_output_mutation=True)
    def load_model():
        model = pipeline("fill-mask", model="bert-base-uncased")
        return model


    model_load_state = st.text('Loading Model...')
    model = load_model()

    # Notify the reader that the data was successfully loaded.
    model_load_state.text('Loading Model...done!')


    st.write("`` ⚠️ ONLY ONE [MASK] is ALLOWED!!``")
    st.write("### Enter Sentence")
    input = st.text_input(" ")
    button = st.button("💡")
    if button and not input:
        st.warning("⚠️ Please INPUT a Sentence ⚠️")

    try:
        with st.spinner("Finding suitable Words"):
            if button and input:
                answers = model(input)
                i=1
                for ans in answers:
                    st.write("``Trial``",i,":",ans["sequence"],"``Score``:", str(ans["score"]))
                    i=i+1

    except PipelineException:
        st.warning("No **[MASK]** Found in Input Sentence")
    except:
        st.warning("Some **Unexpected** Error happen")
        st.warning("Please create a **Issue** on [Github](https://github.com/srajanseth84/FTG)")


    st.markdown("Created by **Srajan Seth**")
    st.markdown(body="""
    <th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
    <th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>
    """, unsafe_allow_html=True)