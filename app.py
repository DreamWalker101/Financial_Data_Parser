import streamlit as st
import pandas as pd
import os
import tempfile
from src.excel_processor import process_excel_file, generate_graphs

st.set_page_config(page_title="📊 Financial Data Parser", layout="wide")
st.title("📈 Financial Data Parser")
st.markdown("Upload your Excel file to analyze data, view statistics, and download summary reports.")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    try:
        df, stats, summary = process_excel_file(tmp_path, output_folder)

        st.success("✅ File processed successfully.")
        st.subheader("📋 Data Preview")
        st.dataframe(df)

        st.subheader("📊 Summary Report")
        st.json(summary)

        st.subheader("📈 Summary Statistics")
        st.dataframe(stats)

        st.subheader("📉 Graphs")
        graphs = generate_graphs(df)
        for fig in graphs:
            st.pyplot(fig)

        st.markdown("📥 Download your summary and statistics reports:")
        summary_filename = f"{summary['filename']}_summary.xlsx"
        stats_filename = f"{summary['filename']}_statistics.xlsx"

        with open(os.path.join(output_folder, summary_filename), "rb") as f:
            st.download_button("Download Summary", f, file_name=summary_filename)

        with open(os.path.join(output_folder, stats_filename), "rb") as f:
            st.download_button("Download Statistics", f, file_name=stats_filename)

    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
