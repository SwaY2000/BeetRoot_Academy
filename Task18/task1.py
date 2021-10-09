def choose_func(nums):
    for i in nums:
        if i < 0 and i is int:
            return square_nums(nums)
        elif i > 0 and i is int:
            remove_negatives(nums)
        else:
            raise TypeError("Not is digit")

def square_nums(nums):
     return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    a = choose_func(nums1)
    b = choose_func(nums2)
    print(a, b)