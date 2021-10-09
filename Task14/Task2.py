def test1():
    print("I'm first function")
    test2()

def test2():
    return print("I'm second function")

test1()