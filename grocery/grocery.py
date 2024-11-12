grcry = {}
while True:
    try:
        item = input()
        if item.upper() in grcry:
            grcry[item.upper()] = grcry[item.upper()]+1
        else:
            grcry[item.upper()] = 1
    except EOFError:
        items = sorted(grcry)
        for i in items:
            print(grcry[i.upper()],i)
        break

