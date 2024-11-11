receive = 0
price = 50
print("Amount Due: ", price)
coin = int(input("Insert Coin: "))
receive += coin
while True:
    if coin in [25,10,5]:
        if price > receive:
            print("Amount Due: ", price-receive)
            coin = int(input("Insert Coin: "))
            receive = receive + coin
            #print(receive)
        else:
            print("Change Owed: ", receive-price)
            break
    else:
        receive = receive - coin
        print("Amount Due: ", price - receive)
        coin = int(input("Insert Coin: "))

