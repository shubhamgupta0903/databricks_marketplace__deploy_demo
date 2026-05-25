import os
import streamlit as st

st.set_page_config(page_title="Marketplace Demo App")

st.title("Databricks Marketplace Demo App")

app_name = os.getenv("APP_NAME", "Default App")
api_key = os.getenv("API_KEY", "No API Key Found")

st.write(f"Application Name: {app_name}")

question = st.text_input("Ask a Question")

if question:
    st.success(f"You asked: {question}")

st.divider()

st.write("Environment Variable Demo")

masked_key = api_key[:4] + "****"

st.code(masked_key)
