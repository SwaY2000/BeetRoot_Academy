# Write
# a
#
#
# class TypeDecorators which has several methods for converting results of functions to a specified type ( if it's possible):
#
# methods:
#
#     to_int
#
#
# to_str
#
# to_bool
#
# to_float
#
# Don
# 't forget to use @wraps
#
# ```
#
#
# class TypeDecorators:
#     pass
#
#
# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string
#
#
# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string
#
#
# assert do_nothing('25') == 25
#
# assert do_something('True') is True
#
# ```


class TypeDecorators:
    def to_int(self):
        def wrapper(*args, **kwargs):
            try:
                return int(*args, **kwargs)
            except ValueError:
                return f"Convert to intenger with help method {__name__} with variables {args, kwargs}, unpossible"
        return wrapper

    def to_str(self):
        def wrapper(*args, **kwargs):
            try:
                return str(*args, **kwargs)
            except ValueError:
                return f"Convert to intenger with help method {__name__} with variables {args, kwargs}, unpossible"
        return wrapper

    def to_bool(self):
        def wrapper(*args, **kwargs):
            try:
                return bool(*args, **kwargs)
            except ValueError:
                return f"Convert to intenger with help method {__name__} with variables {args, kwargs}, unpossible"
        return wrapper

    def to_float(self):
        def wrapper(*args, **kwargs):
            try:
                return float(*args, **kwargs)
            except ValueError:
                return f"Convert to intenger with help method {__name__} with variables {args, kwargs}, unpossible"
        return wrapper


@TypeDecorators.to_int
def do_something(string: str):
    return string

assert do_something("20") == 20

@TypeDecorators.to_str
def do_something(string: str):
    return string

assert do_something("Hi") == "Hi"

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_something("True") is True

@TypeDecorators.to_float
def do_something(string: str):
    return string

assert do_something("50.7") == 50.7


print(do_something("20f"))

# assert do_nothing('25') == 25
#
# assert do_something('True') is True

