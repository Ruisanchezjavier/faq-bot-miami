import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load CSV as if it were Excel
df =  pd.read_csv("sales.csv")

# Analysis
total = df["sales"].sum()
best_day = df.loc[df["sales"].idxmax()]
worst_day = df.loc[df["sales"].idxmin()]
average = df["sales"].mean()

# Print report to terminal
print("=" * 40)
print("     WEEKLY BUSINESS REPORT")
print("=" * 40)
print(f"total revenue    ${total:,}")
print(f"Best day:        {best_day['day']} (${best_day['sales']:,})")
print(f"Worst day:       {worst_day['day']} (${worst_day['sales']:,})")
print(f"Average daily:   ${average:,.2f}")
print("=" * 40)

# Generate PDF report
pdf = SimpleDocTemplate("weekly_report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
elements = []

# Title 
elements.append(Paragraph("Weekly Business Report", styles["Title"]))
elements.append(Spacer(1, 20))

# Summary table
summary_data = [
    ["Metric", "Value"],
    ["Total Revenue", f"${total:,}"],
    ["Best Day", f"{best_day['day']} (${best_day['sales']:,})"],
    ["Worst Day", f"{worst_day['day']} (${worst_day['sales']:,})"],
    ["Average Daily Sales", f"${average:,.2f}"],
]

table = Table(summary_data, colWidths=[250, 200])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.black),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 13),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ("FONTSIZE", (0, 1), (-1, -1), 11),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("PADDING", (0, 0), (-1, -1), 10),
]))

elements.append(table)
pdf.build(elements)
print("\nPDF report saved as weekly_report.pdf")
