# src/reports/pdf_report.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(summary_df, risk_report, file_path="reports/walkforward_report.pdf"):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("WALKFORWARD REPORT", styles['Title']))
    story.append(Spacer(1, 12))

    # Risk report
    story.append(Paragraph("RISK REPORT", styles['Heading2']))
    for key, value in risk_report.items():
        story.append(Paragraph(f"{key}: {value}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Walkforward Summary Table
    story.append(Paragraph("WALKFORWARD SUMMARY", styles['Heading2']))
    data = [summary_df.columns.tolist()] + summary_df.values.tolist()
    table = Table(data)
    story.append(table)

    doc.build(story)
    print(f"PDF report saved at: {file_path}")
