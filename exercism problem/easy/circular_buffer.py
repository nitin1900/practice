#copy-paste from duck ai...

from collections import deque

def ask_overwrite():
    while True:
        choice = input("Deque is full — overwrite oldest? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please answer y or n.")

limited_list = deque(maxlen=7)
while True:
    user = input("Enter anything valid (exit to close): ")
    if user == "exit":
        break
    if len(limited_list) >= limited_list.maxlen:
        if ask_overwrite():
            # overwrite by using append (deque with maxlen will drop leftmost)
            limited_list.append(user)
        else:
            print("Item not added.")
    else:
        limited_list.append(user)

print(limited_list)

#ai...
class BufferFullException(BufferError):
    def __init__(self, message):
        super().__init__(message)

class BufferEmptyException(BufferError):
    def __init__(self, message):
        super().__init__(message)

class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_ptr = 0
        self.write_ptr = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")
        
        data = self.buffer[self.read_ptr]
        self.buffer[self.read_ptr] = None
        self.read_ptr = (self.read_ptr + 1) % self.capacity
        self.size -= 1
        return data

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")
        
        self.buffer[self.write_ptr] = data
        self.write_ptr = (self.write_ptr + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size == self.capacity:
            self.buffer[self.write_ptr] = data
            self.write_ptr = (self.write_ptr + 1) % self.capacity
            self.read_ptr = (self.read_ptr + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_ptr = 0
        self.write_ptr = 0
        self.size = 0

#solution...


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            return self.buffer.pop(0)

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
            self.buffer.append(data)
        else:
            self.buffer.append(data)

    def clear(self):
        self.buffer = []
