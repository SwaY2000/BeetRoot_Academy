def Test():
    a, b, c, d = 1, 2, 3, 4
    #__code__.co_nlocals output overthing locals variablse in function
    return print(Test.__code__.co_nlocals)
Test()