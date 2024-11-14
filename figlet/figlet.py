import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    txt = input("Input:")
    print(figlet.renderText(txt))
elif len(sys.argv) ==3:
    ...
else:
    print("Invalid usage")
    sys.exit()

