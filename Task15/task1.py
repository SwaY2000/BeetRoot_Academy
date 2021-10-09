def decorator(function):
    """It's decorator output sample function name and variables input function"""
    def change_function(*args):
        print("I'm function inside decorator!\n"
              "And I want will show you, with which variablse function run!")
        function(*args)
        print(f"Function {function.__name__} run with {args}")
        print("I'm done myyy work, bayyyy ;)")
    return change_function

@decorator
def add(x, y):
    return x + y

@decorator
def square_all(*args):
    return [i ** 2 for i in args]


add(10, 5)
a = square_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)