string = input("Input:")
twttr =""
for i in string:
    if i not in ['a', 'e', 'i' ,'o', 'u']:
        twttr = twttr + i
print(twttr)

