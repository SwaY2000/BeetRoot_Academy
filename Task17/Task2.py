class in_range:
    def __init__(self, start = -1, end = 1, step = 1):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        self.start += self.step
        if self.start == self.end:
            raise StopIteration
        return self.start

_range = in_range(end = 10)

for i in _range:
    print(i)