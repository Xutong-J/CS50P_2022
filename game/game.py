import random

lv = int(input("Level:"))
ans = random.randint(1,lv)

while lv <= 0:
    lv = int(input("Level:"))

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



