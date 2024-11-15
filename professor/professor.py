import random


def main():
    for _ in range(0,10):
        lv = get_level()
        x, y = generate_integer(lv)
        check(x,y)



def get_level():
    while True:
        try:
            n = int(input("Level:"))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    for _ in range(0,10):
    match level:
        case 1 :
            x = random.randint(0,9)
            y = random.randint(0,9)
        case 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        case _:
            x = random.randint(100,999)
            y = random.randint(100,999)
    return x, y


def check_ans(x , y):
    ...


if __name__ == "__main__":
    main()
