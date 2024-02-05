from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="p", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    # Set the Header
    pdf.set_text_color(90, 90, 90)
    pdf.set_font(family="arial", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    pdf.line(10, 21, 200, 21)

    # Set the Footer
    pdf.ln(265)
    pdf.line(10, 286, 200, 286)
    pdf.set_text_color(130, 130, 130)
    pdf.set_font(family="arial", style="I", size=10)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the Footer
        pdf.ln(277)
        pdf.line(10, 286, 200, 286)
        pdf.set_text_color(130, 130, 130)
        pdf.set_font(family="arial", style="I", size=10)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")