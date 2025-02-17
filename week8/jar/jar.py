class Jar:
    def __init__(self, capacity=12):
        self._cookies = 0
        self.capacity = capacity


    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer.")
        if self._cookies + n > self.capacity:
            raise ValueError("Put in too much cookies!")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer.")
        if self._cookies - n < 0:
            raise ValueError("No such cookies to take!")
        self._cookies -= n

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
