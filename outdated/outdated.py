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
        print(f"{y:04}-{m:02}-{d:02}")
