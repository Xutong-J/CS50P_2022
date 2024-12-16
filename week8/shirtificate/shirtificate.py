from fpdf import FPDF


class PDF(FPDF):
    ...




def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", size=30)
    pdf.cell(200, 10, txt="CS50 Shirtificate", ln=True)
    pdf.image("./shirtificate.png", x=None, y=0, w=190, h=280, keep_aspect_ratio=True)
    pdf.output("example.pdf")

if __name__ == "__main__":
    main()
