# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

unsorted = [19, 8, 7, 18, 14, 10, 1, 17, 20,
            2, 3, 5, 6, 13, 15, 4, 9, 16, 11, 12]
# O(n)


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # variables for the current index of our two arrays
    a = 0
    b = 0
    # merging logic
    for i in range(elements):
        if a >= len(arrA):  # everything in arrA has been merged
            merged_arr.append(arrB[b])
            b += 1
        elif b >= len(arrB):  # everything in arrB has been merged
            merged_arr.append(arrA[a])
            a += 1
        elif arrA[a] < arrB[b]:  # a is smaller, add it to the array
            merged_arr.append(arrA[a])
            a += 1
        else:  # otherwise b is smaller add that instead
            merged_arr.append(arrB[b])
            b += 1
    return merged_arr


# O(n logn)
def merge_sort(arr):
    # 1. While your data set contains more than one item, split it in half
    midpoint = len(arr) // 2
    if len(arr) > 1:
        right = merge_sort(arr[midpoint:])
        left = merge_sort(arr[:midpoint])
        arr = merge(left, right)
    return arr

# 1024
# 512
# 256
# 128
# 64
# 32
# 16
# 8
# 4
# 2
# 1


# def count_down_recursive(n):
#     # base case
#     # what makes our recursion stop
#     if n <= 0:
#         return
#     # recursive case
#     # decrement
#     count_down_recursive(n - 1)
#     print(n)


# count_down_recursive(10)

print(merge_sort(unsorted))
print(unsorted)
