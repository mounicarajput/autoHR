import streamlit as st


import streamlit as st
from langchain.llms import OpenAI
import streamlit as st
import pandas as pd
import numpy as np

st.title('🦜🔗 App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

st.title("Auto HR")

# Submit Button
st.button("Get Started")

