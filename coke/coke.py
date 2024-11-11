receive = 0
price = 50
print("Amount Due: ", price)
coin = input("Insert Coin: ")

if coin in [25,10,5]:
    receive += coin
    if price > receive:
        print("Insert Coin: ", price-receive)
        coin = input("Insert Coin: ")
        receive += coin
    else:
        print("Change Owed: ", receive - price)
else:
    print("Amount Due: ", price - receive)
