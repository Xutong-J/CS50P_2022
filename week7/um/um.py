import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b(um)(?:[\W]+)*"
    return len(re.findall(pattern,s.strip(), re.IGNORECASE))


if __name__ == "__main__":
    main()
