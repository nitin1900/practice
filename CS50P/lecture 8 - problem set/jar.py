class Jar:
    def __init__(self, capacity=12):
        if type(capacity)!=int or capacity<0:
            raise ValueError
        self._capacity=capacity
        self._size=0

    def __str__(self):
        return "🍪"*self._size

    def deposit(self, n):
        if self._size+n>self._capacity:
            raise ValueError
        else:
            self._size=self._size+n

    def withdraw(self, n):
        if n>self._size:
            raise ValueError
        else:
            self._size=self._size-n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size