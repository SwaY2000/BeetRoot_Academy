list1 = [1, 2, 3, 4]
dict1 = {1:"1", 2:"2"}
def indexerr(list1, ind):
    try:
        print(list1[ind])
    except IndexError:
        print("Oopss...\nIndex exit range")
indexerr(list1, 6)
def keyerr(dict1, keyy):
    try:
        print(dict1[keyy])
    except KeyError:
        print("Oopss...\nKey not found")
keyerr(dict1, 5)