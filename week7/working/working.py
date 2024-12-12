import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^[0-9: ]+(AM|PM)$"
    matches = re.search(pattern, s.strip())
    if matches:
        


...


if __name__ == "__main__":
    main()
