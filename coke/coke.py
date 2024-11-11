receive = 0
price = 50
print("Amount Due: ", price)
coin = int(input("Insert Coin: "))

while True:
    if coin in [25,10,5]:
        receive += coin
        if price > receive:
            print("Amount Due: ", price-receive)
            coin = int(input("Insert Coin: "))
            receive += coin
        else:

            break
    else:            print("Change Owed: ", receive - price)
        print("Amount Due: ", price - receive)
        coin = int(input("Insert Coin: "))

