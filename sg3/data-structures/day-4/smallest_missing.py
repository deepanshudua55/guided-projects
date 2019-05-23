""" 
Find the Smallest Missing Element from a Sorted Array
Given a sorted array of distinct non-negative integers, find the smallest missing element in it. 
"""

l = [0, 1, 2, 6, 9, 11, 15]  # outputs 3
l2 = [1, 2, 3, 4, 6, 9, 11, 15]  # outputs 0
l3 = [0, 1, 2, 3, 4, 5, 6]  # outputs 7 - also is the length of the array

# find the first index where the element is not equal to the index


# O(n)
def linear_smallest_missing(arr):
    for idx, num in enumerate(arr):
        if num != idx:
            return idx
    return len(arr)


print(linear_smallest_missing(l))
linear_smallest_missing(l2)
linear_smallest_missing(l3)


# O(log n)
def smallest_missing(arr, start_idx, end_idx):
    # base case is when the start is bigger than the end
    if start_idx > end_idx:
        return start_idx

    midpoint = start_idx + (end_idx - start_idx) // 2

    # check if the item at the midppoint is equal to the index
    if arr[midpoint] == midpoint:
        # search the right half of the array
        return smallest_missing(arr, midpoint + 1, end_idx)
    else:
        # search the left half
        return smallest_missing(arr, start_idx, midpoint - 1)


print(smallest_missing(l, 0, len(l) - 1))
print(smallest_missing(l2, 0, len(l2) - 1))
print(smallest_missing(l3, 0, len(l3) - 1))

