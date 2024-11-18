string = input("Input:")
twttr =""
for i in string:
    if i not in ['a', 'e', 'i' ,'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        twttr = twttr + i
print(twttr)

