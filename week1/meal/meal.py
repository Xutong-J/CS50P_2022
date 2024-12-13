def main():
    t = input("What time is it? ").lower().strip()
    time = convert(t)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18<= time <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    hour = int(h)
    min = int(m)
    return float(hour) + float(min/60)

if __name__ == "__main__":
    main()
