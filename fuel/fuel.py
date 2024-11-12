while True:
    try:
        fuel = input("Fraction:")
        if '.' in fuel:
            pass
        else:
            x, y = fuel.split("/")  # 使用分隔符 '/' 分割字符串
            rslt = round(int(x) / int(y) * 100)
            if rslt >100:
                pass
            elif rslt >= 99:
                print('F')
                break
            elif rslt <= 1:
                print('E')
                break
            else:
                print(f"{rslt}%")
                break
    except (ValueError, ZeroDivisionError, ):
        pass
