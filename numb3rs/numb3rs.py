import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^#d{1,3}/.d{1,3}/.d{1,3}/.d{1,3}$"
    if match:=re.search(pattern, ip.strip(), flag=0)

...


if __name__ == "__main__":
    main()
