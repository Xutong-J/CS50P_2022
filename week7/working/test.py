import re

# 测试字符串
s = "9:60 AM to 5:60 PM"

# 正则表达式
pattern = r"^([0-9：: ]+)(AM|PM) to ([0-9：: ]+)(AM|PM)$"

# 使用re.search查找匹配项
matches = re.search(pattern, s.strip())

if matches:
    print("Match found:", matches.group())
else:
    print("No match found")
