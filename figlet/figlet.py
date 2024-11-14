import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(argv) == 1:
    txt = input("Input:")
    print(figlet.renderText(txt))
elif len(argv) ==3:
    ...
else:
    print("Invalid usage")
    sys.exit()

