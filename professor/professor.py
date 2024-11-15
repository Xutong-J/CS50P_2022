import random


def main():
    for _ in range(0,10):
        lv = get_level()
        x = generate_integer(lv)



def get_level():
    while True:
        try:
            n = int(input("Level:"))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    ...

def check_ans(x , y):
    ...


if __name__ == "__main__":
    main()
