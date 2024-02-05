from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="p", unit="mm", format="a4")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_text_color(90, 90, 90)
    pdf.set_font(family="arial", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")