from fpdf import FPDF

fonts = ["Arial", "Courier", "Times", "Helvetica", "Symbol", "ZapfDingbats"]

pdf = FPDF()
pdf.add_page()

for font in fonts:
    pdf.set_font(font, "", 16)
    # x, y, テキスト, 改行あり
    pdf.cell(0, 10, f"{font} font sample", ln=1)

pdf.output("font_preview_sheet.pdf")
