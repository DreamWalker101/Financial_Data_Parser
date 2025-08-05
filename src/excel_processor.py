import pandas as pd
import os
import matplotlib.pyplot as plt

def process_excel_file(file_path, output_folder):
    file_name = os.path.basename(file_path)
    df = pd.read_excel(file_path)

    summary = {
        'filename': file_name,
        'num_rows': len(df),
        'num_columns': len(df.columns),
        'columns': list(df.columns)
    }

    # Save summary to Excel
    summary_df = pd.DataFrame([summary])
    summary_path = os.path.join(output_folder, f"{file_name}_summary.xlsx")
    summary_df.to_excel(summary_path, index=False)

    # Save statistics
    stats = df.describe(include='all').transpose()
    stats_path = os.path.join(output_folder, f"{file_name}_statistics.xlsx")
    stats.to_excel(stats_path)

    return df, stats, summary

def generate_graphs(df):
    graphs = []

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    for col in numeric_cols:
        fig, ax = plt.subplots()
        df[col].hist(ax=ax, bins=20)
        ax.set_title(f"Distribution of {col}")
        graphs.append(fig)

    return graphs
