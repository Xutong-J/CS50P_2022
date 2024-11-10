


def camel_to_snake(camel_str):
    result = []

    for char in camel_str:
        if char.isupper():
            # 如果是大写字母，转换为小写并在前面加下划线
            if result:
                result.append('_')
            result.append(char.lower())
        else:
            result.append(char)

    return ''.join(result)


string = input("camelCase: ")
print("snake_case: ",camel_to_snake(string))
