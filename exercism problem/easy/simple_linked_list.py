#copy-paste from ai...

class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self._length += 1

    def pop(self):
        if not self.head:
            raise EmptyListException("Playlist is empty")
        val = self.head.data
        self.head = self.head.next
        self._length -= 1
        return val

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def __len__(self):
        return self._length

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def display(self):
        if not self.head:
            raise EmptyListException("Playlist is empty")
        return " -> ".join(map(str, self))


# -------- Interactive Menu --------

playlist = LinkedList()

while True:
    print("\n1. Add Song")
    print("2. Remove Song")
    print("3. Show Playlist")
    print("4. Reverse Playlist")
    print("5. Length")
    print("6. Create from Range")
    print("0. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            song = int(input("Enter song ID: "))
            playlist.push(song)

        elif choice == "2":
            print("Removed:", playlist.pop())

        elif choice == "3":
            print("Playlist:", playlist.display())

        elif choice == "4":
            playlist.reverse()
            print("Playlist reversed")

        elif choice == "5":
            print("Total songs:", len(playlist))

        elif choice == "6":
            start = int(input("Start ID: "))
            end = int(input("End ID: "))
            for i in range(start, end + 1):
                playlist.push(i)
            print("Playlist created")

        elif choice == "0":
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)

#solution...





class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._count = 0
        for v in values:
            self.push(v)

    def __len__(self):
        return self._count

    def head(self):
        if self._head is None:
            raise EmptyListException('The list is empty.')
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._count += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException('The list is empty.')
        value = self._head.value()
        self._head = self._head.next()
        self._count -= 1
        return value

    def reversed(self):
        return LinkedList(self)

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()


class EmptyListException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
