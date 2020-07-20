def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    found = False
    start = 0
    end = len(arr) - 1
    last = 0

    while not found:
        middle = (start + end) // 2

        if last == middle or last - middle == 1:
            return -1
        elif arr[middle] == target:
            return arr.index(arr[middle])
        elif target > arr[middle]:
            start = middle
            last = middle
        else:
            end = middle
            last = middle

    return -1  # not found
