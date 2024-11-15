import random


def main():
    lv = get_level()
    x = generate_integer(lv)
    y = generate_integer(lv)
    

def get_level():
    while True:
        try:
            n = int(input("Level:"))
            if n > 0:
                return n
        except ValueError:
            pass

def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
