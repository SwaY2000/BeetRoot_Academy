
class Fraction:
    def __init__(self, nominator: int, denominator: int):
        self.nominator = self.__if_digit(nominator)
        self.denominator = self.__if_digit(denominator)

    def __str__(self):
        return f"Your fraction: {self.nominator}/{self.denominator}"

    def __if_digit(self, digit):
        """If digit for init"""
        self.digit = digit
        if type(self.digit) == int:
            pass
        elif type(self.digit) != int:
            raise ValueError("Values must be intenger")
        return self.digit

    def culc(self, unar: str, y):
        """Parents function"""
        self.__if_unar(unar, y)

    def __if_unar(self, unar, y):
        """This is function checks, which unarniy operator choose users and makes culculation """
        if self.denominator >= y.denominator:
            if unar == "+":
                self.__general_amount(y, self)
                self.nominator += y.nominator
                return self
            elif unar == "-":
                self.__general_amount(y, self)
                self.nominator -= y.nominator
            elif unar == "*":
                self.nominator *= y.nominator
                self.denominator *= y.denominator
            elif unar == "/":
                #reverse fraction
                y.nominator, y.denominator = y.denominator, y.nominator
                self.nominator *= y.nominator
                self.denominator *= y.denominator
        if self.denominator < y.denominator:
            if unar == "+":
                self.__general_amount(self, y)
                self.nominator += y.nominator
                return self
            elif unar == "-":
                self.__general_amount(self, y)
                self.nominator -= y.nominator
            elif unar == "*":
                self.nominator *= y.nominator
                self.denominator *= y.denominator
            elif unar == "/":
                #reverse fraction
                self.nominator, self.denominator = self.denominator, self.nominator
                y.nominator *= self.nominator
                self.nominator = y.nominator
                y.denominator *= self.denominator
                self.denominator = y.denominator

    def __general_amount(self, less_digit, more_digit):
        """Find general amount, for values denominator
        less_digit is digit which has lesses denominator than denominator more_digit(I hope you understand)
        So, exmpl: less_digit = 1/3 and more_digit = 1/7, more digit has denominator 7, which mor denomunator
        less_digit 3"""
        for i in range(1, 10):
            if less_digit.denominator * i == more_digit.denominator:
                print(i)
                less_digit.denominator *= i
                less_digit.nominator *= i
                # self.nominator += y.nominator
                return more_digit, less_digit
        for i in range(1, 100):
            for j in range(1, 100):
                if more_digit.denominator * i == less_digit.denominator * j:
                    more_digit.denominator *= i
                    more_digit.nominator *= i
                    less_digit.denominator *= j
                    less_digit.nominator *= j
                    #return print(f"Succsesfull! X denomiunator: {x.nominator, x.denominator},"
                     #            f" Y = {y.nominator, y.denominator}")

x = Fraction(2, 2)
y = Fraction(5, 10)
x.culc("-",y)
print(x)
