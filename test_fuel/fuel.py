def main():
    while True:
        try:
            print(gauge(convert(input("Fraction:"))))
        except (ValueError, ZeroDivisionError, ):
            pass

def convert(fraction):
    x, y = fraction.split("/")  # 使用分隔符 '/' 分割字符串
    if ('.' in x+y) or (x > y):
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f"{rslt}%"


if __name__ == "__main__":
    main()
