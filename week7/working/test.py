s = input("Time")
pattern = r"^([0-9\: ]+)(AM|PM) to ([0-9\: ]+)(AM|PM)$"
matches = re.search(pattern, s.strip())
print(matches)
