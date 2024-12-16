class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._cookies = 0

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        self._cookies -= n

    def withdraw(self, n):
        self._cookies += n

    #Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    #Setter for capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise ValueError("Capacity Invalid!")
        self._capacity = capacity
        if self._cookies > self._capacity:
            raise ValueError("Too much cookies!")
        if self.cookies < 0:
            raise ValueError("No much cookies!")

    @property
    def size(self):
        return self._cookies

def main():
    jar = Jar(10)
    print(f"Number of cookies: {jar}")
    jar.deposit(int(input("How many cookies do you want to put?")))
    print(f"Number of cookies: {jar}")
    jar.withdraw(int(input("How many cookies do you want to withdraw?")))
    print(f"Number of cookies: {jar}")


if __name__ == "__main__":
    main()
