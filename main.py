from fpdf import FPDF
#install fpdf package

import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="letter")
# P=portrait and all dimentions are in mm
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")

for index, row in df.itterows():
    pdf.add_page()

    #Sets header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=["Topic"], align="L",
         ln=1)
    pdf.line(10, 21, 200, 21)

    pdf.ln(277)

    #Making the footer for the master page
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.ln(277)
        # Making the footer for the rest of the pages
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")