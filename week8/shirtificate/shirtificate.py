from fpdf import FPDF


class PDF(FPDF):
    ...




def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Hello, World!", ln=True)
    pdf.image("./shirtificate.png", x=None, y=0, w=210, h=297, keep_aspect_ratio=True)
    pdf.output("example.pdf")

if __name__ == "__main__":
    main()
