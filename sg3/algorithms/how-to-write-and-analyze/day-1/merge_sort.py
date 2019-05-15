"""
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
"""

# O(n)
# TO-DO: complete the helpe function below to merge 2 sorted arrays
unsorted = [14, 4, 11, 8, 7, 1, 9, 19, 13,
            17, 5, 3, 16, 18, 2, 20, 10, 15, 6, 12]

# merge two sorted arrays and merges them into one sorted array


def merge(arr_a, arr_b):
    elements = len(arr_a) + len(arr_b)  # O(1)
    # creates an array of all 0s equal to the length of the two combined arrays
    merged_arr = []  # O(1)
    # TO-DO
    # create variables for the current index of a and the current index of b
    # every time an element is merged from A or B, we increment the counter
    a = 0  # O(1)
    b = 0  # O(1)
    # create a for loop that loops from 0 to elements
    for i in range(elements):  # O(n)
        # all the elements of A have been merged
        if a >= len(arr_a):  # O(1)
            # add the current element in B
            merged_arr.append(arr_b[b])  # O(1)
            # increment b
            b += 1  # O(1)
        # all the elements of B have been merged
        elif b >= len(arr_b):  # O(1)
            # add the current element in A
            merged_arr.append(arr_a[a])  # O(1)
            # increment a
            a += 1  # O(1)
        # the current element in A is smaller than the current element in B
        elif arr_a[a] < arr_b[b]:  # O(1)
            # add the current element in A
            merged_arr.append(arr_a[a])  # O(1)
            # increment a
            a += 1  # O(1)
        # the current element in B is smaller than the current element in A
        else:
            # add the current element in A
            merged_arr.append(arr_b[b])  # O(1)
            # increment a
            b += 1  # O(1)

    return merged_arr

# [1, 3], [2, 4] -> [1, 2, 3, 4]
# [1, 2], [3, 4]


print(merge([1, 3], [2, 4]))  # [1, 3], [2, 4] -> [1, 2, 3, 4]

# TO-DO: implement the Merge Sort function below USING RECURSION


# O(n logn)
def merge_sort(arr):
    # TO-DO
    midpoint = len(arr) // 2
# 1. While your data set contains more than one item, split it in half
    if len(arr) > 1:
        # split it in half
        # O(log n)
        left = merge_sort(arr[:midpoint])
        right = merge_sort(arr[midpoint:])
        # O(n)
        arr = merge(left, right)
    return arr


print(merge_sort(unsorted))
