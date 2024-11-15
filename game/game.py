import random

ans = random.randint(1,lv)
try:
    lv = int(input("Level:"))
while lv <= 0:
    lv = int(input("Level:"))
except


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



