class FibanachiSerach:
    def __init__(self):
        self.i = 0
        self.p = 0
        self.q = 0
        self.stop = False

    def get_fibonacci_number(self, k):
        first_number = 0
        second_number = 1
        n = 0
        while n < k:
            temp_number = second_number
            second_number = first_number + second_number
            first_number = temp_number
        return first_number

    def start_init(self, sequince: list):
        self.stop = False
        k = 0
        n = len(sequince)
        while (self.get_fibonacci_number(k+1) < len(sequince)):
            k = k+1
        m = self.get_fibonacci_number(k+1)-(n+1)
        self.i = self.get_fibonacci_number(k) - m
        self.p = self.get_fibonacci_number(k-1)
        self.q = self.get_fibonacci_number(k-2)

    def up_index(self):
        if self.p == 1:
            self.stop = True
        self.i = self.i - self.q
        temp = self.q
        self.q = self.p - self.q
        self.p = temp

    def down_index(self):
        if self.q == 0:
            self.stop = True
        self.i = self.i - self.q
        temp = self.q
        self.q = self.p - self.q
        self.p = temp

    def search(self, sequince, element):
        self.start_init(sequince)
        result_index = -1
        while not self.stop:
            if self.i < 0:
                self.up_index()
            elif self.i >= len(sequince):
                self.down_index()
            elif sequince[self.i] == element:
                result_index = self.i
                break
            elif element < sequince[self.i]:
                self.down_index()
            elif element > sequince[self.i]:
                self.up_index()
        return result_index


if __name__ == '__main__':
    sequince = [-2, 1, 2, 3, 4, 5, 6, 7]

    fs = FibanachiSerach()

    element = 1

    print(fs.search(sequince, element))