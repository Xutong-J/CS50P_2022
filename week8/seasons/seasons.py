from datetime import date
import sys
import re


def main():
    birthday = get_birth()



def get_birth():
    birth = input("Date of Birth: ")
    matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth)
    if matches:
        year = matches.group(1)
        month = matches.group(2)
        day = matches.grop(3)
    else:
        sys.exit()

    return date(year, month, day)


if __name__ == "__main__":
    main()
