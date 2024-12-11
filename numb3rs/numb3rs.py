import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    matches=re.search(pattern, ip.strip())
    if matches:
        for n in range(1,5):
            if 0 > int(matches.group(n)) or int(matches.group(n)) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
