import random
#重复操作可以编成函数来简化程序
#could make a function to reduce repetitive code
while True:
    try:
        lv = int(input("Level:"))
        if lv <= 0:
            pass
        else:
            ans = random.randint(1,lv)
            break
    except (ValueError):
        pass

while True:
    try:
        guess = int(input("Guess:"))
        if guess <= 0:
            pass
        else:
            break
    except (ValueError):
        pass

while True:
    if guess == ans:
        print("Just right!")
        break
    elif guess > ans:
        print("Too large!")
    else:
        print("Too small!")



