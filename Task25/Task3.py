from typing import Optional
def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with postive integers")
    elif n == 0:
        return 0
    elif n == 1:
        return a
    elif n > 1:
        return a + mult(a, n-1)

mult(2, 4)
mult(2, 0)
mult(2, -4)