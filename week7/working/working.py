import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9:]) (AM|PM) to ([0-9:]) (AM|PM)$"
    matches = re.search(pattern, s.strip())
    if matches:
        t1, t2 = matches.group(1), matches.group(3)
        flag1, flag2 = matches.group(2), matches.group(4)
        return process(t1, flag1)+" to "+process(t2,flag2)


def process(t, flag):
    if ':' in t:
        h, m = value(int(t.split(':').strip()))
    else:
        h = int(t)
        m = 0

    if flag == "PM":
        h = 12 + h
    return f"{h:02}:{m:02}"


def value(h,m=None):
    if (m >60 or m==None) or h>12:
        raise ValueError
    else:
        return h,m


if __name__ == "__main__":
    main()
