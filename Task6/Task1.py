some_sentence = input("some text")
dict1 = dict()
for i in some_sentence:
    k = 0
    for j in some_sentence:
        if i == j:
            k += 1
    dict1.update({i:k})
print(dict1)