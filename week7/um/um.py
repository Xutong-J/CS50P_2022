import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(?:[^0-9a-zA-Z]+)(um  )"


...


if __name__ == "__main__":
    main()
