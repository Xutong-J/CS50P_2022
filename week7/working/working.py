import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9:]) (AM|PM) to ([0-9:]) (AM|PM)$"
    matches = re.search(pattern, s.strip())
    if matches:
        t1, t2 = int(matches.group(1)), int(matches.group(3))
        flag1, flag2 = matches.group(2), matches.group(4)


def process(t, flag):
    if ':' in t:
        h, m = t.split(':')
        if

def value(h,m=None):
    if m:
        if m >60 or h>12:
            raise ValueError
    else:
        return h,m
...


if __name__ == "__main__":
    main()
