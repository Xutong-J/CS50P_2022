from datetime import date
import sys
import re
from inflect import engine


def main():
    birthday = get_birth(input("Date of Birth: "))
    today = date.today()
    print(calculate(birthday,today))

def get_birth(birth):
    matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth)
    if matches:
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
    else:
        sys.exit()

    return date(year, month, day)

def calculate(date1,date2):
    days_to_birthday = abs(date1 - date2).days
    p = engine()
    return f"{p.number_to_words(days_to_birthday*24*60, andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
