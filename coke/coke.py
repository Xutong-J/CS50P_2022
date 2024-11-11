receive = 0
price = 50
print("Amount Due: ", price)
coin = int(input("Insert Coin: "))

while receive < price:
    if coin in [25,10,5]:
        receive += coin
        if price > receive:
            print("Amount Due: ", price-receive)
            coin = int(input("Insert Coin: "))
            receive += coin
        else:
            print("Change Owed: ", receive - price,1)
            break
    else:
        print("Amount Due: ", price - receive)
        coin = int(input("Insert Coin: "))

