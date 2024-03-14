import os.path
from datetime import datetime

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from src.reporting import generate_report
from src.utils import generate_data

st.title("Data drift")

min_date = datetime(2023, 1, 1)
max_date = datetime(2024, 1, 1)
if st.sidebar.button("Refresh") or not os.path.exists("data/data.pq"):
    os.makedirs("data", exist_ok=True)
    generate_data()
with st.sidebar.form("form"):
    d1, d2 = st.date_input(
        "Date range",
        (min_date, max_date),
        min_date,
        max_date
    )
    st.form_submit_button("Submit")

df = pd.read_parquet("data/data.pq").set_index("created")

report = generate_report(
    reference_data=df.loc[:"2023-01-01"],
    current_data=df.loc[d1:d2]
)

components.html(
    report, width=1000, height=1200, scrolling=True
)
