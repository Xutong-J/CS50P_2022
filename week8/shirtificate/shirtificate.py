from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 40)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')


def main():
    # 创建PDF对象
    pdf = Shirtificate()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)

    # 添加标题
    pdf.header()

    # 添加图片
    pdf.image('shirtificate.png', x=None, y=0, w=190,keep_aspect_ratio=True)

    # 添加用户名字
    pdf.set_font('Arial', 'B', 18)
    pdf.set_text_color(255, 255, 255)  # 白色文本
    pdf.cell(0, 10, "Jiang Xianfu took CS50", 0, 0, 'C')

    # 输出PDF文件
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()
