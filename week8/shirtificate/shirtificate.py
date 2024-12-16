from fpdf import FPDF


class PDF(FPDF):
    ...




def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Hello, World!", ln=True)
    pdf.image("./shirtificate.png", x=10, y=10, w=80)
    pdf.output("example.pdf")

if __name__ == "__main__":
    main()
