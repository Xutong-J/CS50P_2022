import random


def main():
    score = 0
    lv = get_level()
    for _ in range(0,10):
        x, y = generate_integer(lv)
        if check_ans(x,y):
            score += 1
    print("Score :",score)



def get_level():
    while True:
        try:
            n = int(input("Level:"))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
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
    for _ in range(0,3):
        try:
            ans = int(input(f"{x} + {y} ="))
            if ans == x + y:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

if __name__ == "__main__":
    main()
