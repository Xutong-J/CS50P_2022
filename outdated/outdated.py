def check_print(y, m, d):
    if int(d) <= 31 and int(m) <= 12:
        print(f"{y:04}-{int(m):02}-{int(d):02}")
        return True
    else:
        return False

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
        m.strip()
        if check_print(y, m, d):
            break
        else:
            pass
    elif ',' in date:
        md, y = date.split(', ')
        m, d = md.split(' ')
        if m in month:
            n=0
            for i in month:
                n += 1
                if i == m:
                    break
            m = n
            n = 0
            if check_print(y, m, d):
                break
            else:
                pass
        else:
            pass

    else:
        pass

