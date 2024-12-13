import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(?:[\D\W\b]+)*(um)(?:[\D\W]+)*"


...


if __name__ == "__main__":
    main()
