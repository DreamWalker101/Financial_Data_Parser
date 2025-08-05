import os
from src.excel_processor import process_excel_file
import pandas as pd

DATA_FOLDER = 'data/sample'
OUTPUT_FOLDER = 'output'

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    all_summaries = []

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(DATA_FOLDER, filename)
            file_summary = process_excel_file(file_path, OUTPUT_FOLDER)
            all_summaries.extend(file_summary)

    if all_summaries:
        summary_df = pd.DataFrame(all_summaries)
        summary_path = os.path.join(OUTPUT_FOLDER, "summary_report.xlsx")
        summary_df.to_excel(summary_path, index=False)
        print(f"\n✅ Summary report saved to: {summary_path}")
    else:
        print("❌ No Excel files found.")

if __name__ == '__main__':
    main()
