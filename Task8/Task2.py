def not_normall():
    try:
        a, b = int(input()), int(input())
        print(a**2/b)
    except ValueError:
        print(f"You type not integer")
    except ZeroDivisionError:
        print(f"You type second digit 0")

not_normall()