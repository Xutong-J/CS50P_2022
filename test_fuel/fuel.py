def main():
    while True:
        try:
            print(gauge(convert(input("Fraction:"))))
            break
        except (ValueError, ZeroDivisionError, ):
            pass

def convert(fraction):
    x, y = fraction.split("/")  # 使用分隔符 '/' 分割字符串
    if y == '0':
        raise ZeroDivisionError
    if ('.' in x+y) or (int(x)> int(y)):
        raise ValueError
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
