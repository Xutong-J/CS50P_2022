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
    if


