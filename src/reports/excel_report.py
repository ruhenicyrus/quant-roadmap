# src/reports/excel_report.py

import pandas as pd

def generate_excel_report(summary_df, risk_report, file_path="reports/walkforward_report.xlsx"):
    writer = pd.ExcelWriter(file_path, engine="openpyxl")

    summary_df.to_excel(writer, sheet_name="Summary", index=False)

    # Risk report as DataFrame
    risk_df = pd.DataFrame(list(risk_report.items()), columns=["Metric", "Value"])
    risk_df.to_excel(writer, sheet_name="Risk", index=False)

    writer.save()
    print(f"Excel report saved at: {file_path}")
