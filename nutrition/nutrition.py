Nutri={
    "Apple":130,
    "Avocado":50,
    "Sweet Cherries":100
}
fruit=input("Item:")
if fruit.capitalize() in Nutri:
    print("Calories:",Nutri[fruit])
