grcry = {}
while True:
    try:
        item = input()
        grcry[item.upper()] = grcry
    except EOFError:
        for i in sorted(grcry):
            print(i)

