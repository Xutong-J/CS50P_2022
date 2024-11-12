grcry = {}
while True:
    try:
        item = input()
        grcry[item.upper()] = None
    except EOFError:
        for i in sorted(grcry):
            print(i)

