#Homework:
# Task 1
# Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, *item):
        for i in item:
            self._items.append(i)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

if __name__ == "__main__":
    a = Stack()
    a.push(*[i for i in range(10)])
    print(a)