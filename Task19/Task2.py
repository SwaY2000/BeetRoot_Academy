from sys import path

# path.append("C:/Users/Alx/PycharmProjects/Task19/folder_for_task1/")
# import test

print(path)
def __count_lines(file_name):
    with open(file_name) as file_n:
        return len(file_n.readlines())
print(__count_lines("folder_for_task1/test.txt"))

# from model_for_task1 import im_cool_function
#
# im_cool_function()