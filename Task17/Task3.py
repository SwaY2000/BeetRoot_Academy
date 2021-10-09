class factorial:
    """It's class iteration show "way" factorial, example, factorial 3! have "way"
    3!=1*2*3 and output solution"""
    def __init__(self, start=1, end=1):
        self.start = start
        self.end = end
        self.way_factorial = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        self.start += 1
        self.answear = "I'm in way"
        self.way_factorial = self.way_factorial*self.start
        if self.start == self.end:
            self.answear = self.way_factorial
        return f"Way factorial: {self.way_factorial}, Answear:  {self.answear}"


test = factorial(end=10)

for i in test:
    print(i)