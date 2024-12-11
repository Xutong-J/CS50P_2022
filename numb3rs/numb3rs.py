import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    matches=re.search(pattern, ip)
    if matches:
        for n in range(1,5):
            if 0 > int(matches.group(n)) and int(matches.group(n)) > 255:
                return "False"
        return "True"
    return "False"


if __name__ == "__main__":
    main()
