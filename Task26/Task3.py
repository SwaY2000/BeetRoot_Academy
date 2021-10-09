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

    def get_from_stack(self, find_item):
        for ind, item in enumerate(reversed(self._items), 1):
            if item == find_item:
                return f"Stack: {item} under number {ind}"
        else:
            raise ValueError("Item not found")

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    a = Stack()
    a.push(*[i for i in range(10)])
    print(a.get_from_stack(9))


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, *item):
        for i in item:
            self._items.insert(0, i)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_queue(self, find_item):
        for ind, item in enumerate(reversed(self._items), 1):
            if item == find_item:
                return f"Queue: {item} under number {ind}"
        else:
            raise ValueError("Item not found")

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    a = Queue()
    a.enqueue(*[i for i in range(10)])
    print(a.get_from_queue(9))

