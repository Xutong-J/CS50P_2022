import random

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



