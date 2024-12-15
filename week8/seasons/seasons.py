from datetime import date
import sys
import re


def main():
    birth = input("Date of Birth: ")
    matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$")
    if matches:
        year = matches.group(1)
        month = matches.group(2)
        day = matches.grop(3)
    else:
        sys.exit()



...


if __name__ == "__main__":
    main()
