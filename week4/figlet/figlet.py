import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
txt =''

if len(sys.argv) == 1:
    txt = input("Input:")
    print(figlet.renderText(txt))
elif len(sys.argv) ==3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
        txt = input("Input:")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(txt))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

