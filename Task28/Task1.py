def binary_search(list: list, item, start = None, high = None):
    if high is None and start is None:
        start, high = 0, len(list)-1
    """Search index finding item"""
    mid = (start+high) // 2

    if list[mid] == item:
        return mid

    else:
        if list[mid] < item:
            start = mid
            return binary_search(list, item, start, high)

        elif list[mid] > item:
            high = mid
            return binary_search(list, item, start, high)


print(binary_search([i for i in range(1000)], 65))
