from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')



def main():
    # 创建PDF对象
    pdf = Shirtificate()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    # 获取用户输入的名字
    name = input("Please enter your name: ")

    # 添加标题
    pdf.header()

    # 添加图片
    pdf.image('shirtificate.png', x=(pdf.w - 100) / 2, y=50, w=100)

    # 添加用户名字
    pdf.set_font('Arial', 'B', 18)
    pdf.set_text_color(255, 255, 255)  # 白色文本
    pdf.cell(0, 10, name, 0, 0, 'C')

    # 输出PDF文件
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()
