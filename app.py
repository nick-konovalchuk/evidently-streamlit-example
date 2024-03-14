import os.path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from src.reporting import generate_report
from src.utils import generate_samples


st.title("Data drift")

if (
    st.sidebar.button("Refresh")
    or not os.path.exists("data/ref.pq")
    or not os.path.exists("data/prod.pq")
):
    os.makedirs("data", exist_ok=True)
    generate_samples()

ref = pd.read_parquet("data/ref.pq").set_index("created")
prod = pd.read_parquet("data/prod.pq").set_index("created")

min_date = prod.index.min()
max_date = prod.index.max()

with st.sidebar.form("form"):
    d1, d2 = st.date_input("Date range", (min_date, max_date), min_date, max_date)
    st.form_submit_button("Submit")

report = generate_report(reference_data=ref, current_data=prod)

components.html(report, width=1000, height=1200, scrolling=True)
