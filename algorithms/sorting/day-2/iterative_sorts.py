unsorted = [19, 8, 7, 18, 14, 10, 1, 17, 20,
            2, 3, 5, 6, 13, 15, 4, 9, 16, 11, 12]


def selection_sort(arr):

    # Start with current index = 0
    # For all indices EXCEPT the last index:
    for i in range(len(arr) - 1):
        smallest_index = i
        # a. Loop through elements on right-hand-side of current index and find the smallest element
        for j in range(i, len(arr)):
            # compare the sizes
            if arr[j] < arr[smallest_index]:
                # if smaller, set the smallest index to j
                smallest_index = j
        # more straightforward way
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp
        # b. Swap the element at current index with the smallest element found in above loop
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# selection_sort(unsorted)
# print(unsorted)


def bubble_sort(arr):
    swapped = True
    while swapped:
        print("this is from our while loop")
        print(arr)
        swapped = False
        # if the for loop does no swaps, the while loop will stop after the first iteration
        # iterate to length minus one because we're comparing everything to the element in front
        # Loop through your array
        for i in range(len(arr) - 1):
            # Compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    print("this is from our return statement")
    print(arr)
    return arr


bubble_sort(unsorted)
print("second invokation of bubble_sort")
bubble_sort(unsorted)