class with_index:
    def __init__(self, _list):
        self._list = _list
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i+1 > len(self._list):
            raise StopIteration
        return (self.i, self._list[self.i])

test = with_index([12344, 243243, 5323423, 443243])

for i in test:
    print(i)