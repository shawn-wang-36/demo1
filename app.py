import streamlit as st
import pandas as pd

st.title("Demo Streamlit Dashboard")

data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})

st.subheader("Sample Data")
st.dataframe(data)

st.subheader("Bar Chart")
st.bar_chart(data.set_index('Category'))
