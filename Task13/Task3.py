def choose_func(nums):
    flag = True
    for i in nums:
        if i < 0:
            flag = False
    if flag == True:
        return square_nums(nums)
    else:
        return remove_negatives(nums)

def square_nums(nums):
     return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
a = choose_func(nums1)
b = choose_func(nums2)
print(a, b)