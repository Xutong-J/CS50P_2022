import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b(um)(?:[\W]+)*"
    return len(re.findall(pattern,s.strip()))


if __name__ == "__main__":
    main()
