import inflect

p = inflect.engine()

names = []
try:
    while True:
        name= input("Name:")
        names.append(name)
except EOFError:
    all_names = p.join(names)
    print("\nAdieu, adieu, to",all_names)

