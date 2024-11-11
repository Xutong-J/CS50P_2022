receive = 0
price = 50
print("Amount Due: ", price)
coin = input("Insert Coin: ")

if coin 
receive += coin
if price > receive:
    print("Insert Coin: ", price-receive)
    coin = input("Insert Coin: ")
    receive += coin
else:
    print("Change Owed: ", receive - price)
