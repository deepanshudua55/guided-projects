
# TO-DO: Complete the selection_sort() function below

"""
Start with current index = 0

For all indices EXCEPT the last index:

a. Loop through elements on right-hand-side of current index and find the smallest element

b. Swap the element at current index with the smallest element found in above loop
"""

unsorted = [14, 4, 11, 8, 7, 1, 9, 19, 13,
            17, 5, 3, 16, 18, 2, 20, 10, 15, 6, 12]


# O(n - 1 * O(.5n)) -> O(n^2)
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):  # O(n - 1)
        cur_index = i  # O(1)
        smallest_index = cur_index  # O(1)
        # TO-DO: find next smallest element
        # a. Loop through elements on right-hand-side of current index and find the smallest element
        for j in range(cur_index, len(arr)):  # O(n - i) -> average would be O(.5n) -> O(n)
            if arr[j] < arr[smallest_index]:  # O(1)
                smallest_index = j  # O(1)
        # TO-DO: swap
        # b. Swap the element at current index with the smallest element found in above loop
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]  # O(1)
    print(arr)
    return arr


selection_list = unsorted.copy()
selection_sort(selection_list)

"""
Loop through your array
Compare each element to its neighbor
If elements in wrong position (relative to each other, swap them)
If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
"""

# O(n) - best case with sorted array
# Average and worst - O(n^2)


def bubble_sort(arr):
    swapped = True
    while swapped:
        # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        swapped = False
        # Loop through your array
        # go to length - 1 because we're comparing everything to the element in front
        # if we don't we'll get an IndexError
        for j in range(len(arr) - 1):
            # Compare each element to its neighbor
            if arr[j] > arr[j + 1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    print(arr)
    return arr


bubble_list = unsorted.copy()
bubble_sort(bubble_list)


# O(n + k) - we must know the maximum
def count_sort(arr, maximum=-1):
    count_arr = [0] * maximum
    print(count_arr)
    for i in arr:
        # increment the count of the number
        count_arr[i - 1] += 1
    print(count_arr)
    # incrementer
    j = 0
    for i in range(len(count_arr)):
        while count_arr[i] > 0:
            # set the current index of j to be the number
            arr[j] = i + 1
            # increment j
            j += 1
            # decrement the count
            count_arr[i] -= 1
    print(arr)
    return arr


count_list = unsorted.copy()
count_sort(count_list, 20)
