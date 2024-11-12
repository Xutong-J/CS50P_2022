menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
items = []
while True:
    try:
        items.append(input("Item:"))
        price = 0.00
        for item in items:
            price += menu[item.title()]
        print(f"Total: ${price:.2f}")
    except EOFError:
        price = 0
        items = []
        break
    except KeyError:
        pass



