class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        ...

    def __str__(self):
        cookies = ['🍪'] * self.num
        return "🍪"

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
