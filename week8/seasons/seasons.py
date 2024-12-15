from datetime import date
import sys
import re
from inflect import engine


def main():
    birthday = get_birth()
    today = date.today()
    days_to_birthday = abs(today - birthday).days
    p = engine()
    print(p.number_to_words(days_to_birthday*24, andword=""))

def get_birth():
    birth = input("Date of Birth: ")
    matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth)
    if matches:
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
    else:
        sys.exit()

    return date(year, month, day)


if __name__ == "__main__":
    main()
