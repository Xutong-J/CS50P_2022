class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number of cookies to deposit must be non-negative.")
        if self._cookies + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity.")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Number of cookies to withdraw must be non-negative.")
        if self._cookies - n < 0:
            raise ValueError("Cannot withdraw more cookies than are in the jar.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        if self._cookies > value:
            raise ValueError("Cannot set a new capacity that is less than the current number of cookies.")
        self._capacity = value

    @property
    def size(self):
        return self._cookies

def main():
    jar = Jar(10)
    print(f"Number of cookies: {jar}")
    while True:
        try:
            how_many = int(input("How many cookies do you want to put? "))
            jar.deposit(how_many)
            break
        except ValueError:
            print("Please enter a valid number of cookies.")
    print(f"Number of cookies: {jar}")

    while True:
        try:
            how_many = int(input("How many cookies do you want to withdraw? "))
            jar.withdraw(how_many)
            break
        except ValueError:
            print("Please enter a valid number of cookies.")

    print(f"Number of cookies: {jar}")

if __name__ == "__main__":
    main()
