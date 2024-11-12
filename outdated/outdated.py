month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date:")
    if '/' in date:
        m, d, y = date.split('/')
        print(f"{y:04}-{int(m):02}-{int(d):02}")
        break
    elif ',' in date:
        md, y = date.split(', ')
        m, d = md.split(' ')
        if m in month:
            n=0
            for i in month:
                n+1
                if i == m:
                    break
            m = n
            print(f"{y:04}-{int(m):02}-{int(d):02}")
            break
        else:
            pass

    else:
        pass



