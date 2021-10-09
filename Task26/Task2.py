# Task 2
# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

from typing import Union

class CheckBallance:
    def __init__(self, item: Union[list, str]):
        self._items = self._push(*item)
        self._items = self._check()

    def _push(self, *item: Union[list, str]):
        self._items = []
        for i in item:
            self._items.append(i)
        return self._items

    def _check(self):
        check_square, check_curly, check_round = 0, 0, 0
        for i in self._items:
            if i in ['[', '{', '(']:
                if i in '[':
                    check_square += 1
                elif i in '{':
                    check_curly += 1
                elif i in '(':
                    check_round += 1
            elif i in [']', '}', ')']:
                if i in ']':
                    check_square -= 1
                elif i in '}':
                    check_curly -= 1
                elif i in ')':
                    check_round -= 1
        if check_square == 0 and check_curly == 0 and check_square == 0:
            return 'Balanced'
        else:
            return "Unbalanced"



    def __repr__(self):
        return f"{self._items}"


if __name__ == "__main__":
    a = CheckBallance('(([]))')
    print(a)
    a = CheckBallance('({([]))}')
    print(a)