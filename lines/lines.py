import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
file_name = sys.argv[1]
if file_name[-3:] == '.py':
    try:
        with open(file_name,'r') as f:
            lines = f.readlines()
        if lines and lines[-1].strip() == "":
            lines.pop()  # 删除最后一行空白行

        print(len(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")
