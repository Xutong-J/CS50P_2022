import random

ans = random.randint(1,lv)
while True:
    try:
        lv = int(input("Level:"))
    if lv <= 0:
        pass
    else:
        break
    except (ValueError, ZeroDivisionError):
        pass


guess = int(input("Guess:"))
while lv <= 0:
    guess = int(input("Guess:"))
while True:
    if guess == ans:
        print("Just right!")
        break
    elif guess > ans:
        print("Too large!")
    else:
        print("Too small!")



