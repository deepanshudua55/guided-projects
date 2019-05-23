""" Merge M Sorted Lists of Variable Length
Given M sorted lists of variable length, print them out in sorted order efficiently. """

# make an array from all of the input arrays
# sort that
# return the result

lists = [[10, 20, 30, 40], [32, 33], [15, 25, 35], [27, 29, 37, 48, 93]]


# O(n log n)
def merge_m_lists_sort(lists):
    result = []
    for arr in lists:
        result.extend(arr)
    result.sort()
    return result


print(merge_m_lists_sort(lists))

# Min Heap solution
# we can insert the first element from each list into the heap
[10, 15, 32, 27]
# we delete from the heap
# replace the top element with the item at the last index
# do _sift_down to re-arrange the heap
[27, 15, 32]
[15, 27, 32]
# insert 20 and do bubble_up
[15, 27, 32, 20]
[15, 20, 32, 27]

# O(m log n)
# m = number of lists


def merge_m_lists(lists):
    minheap = Heap()

    for i in range(len(lists)):
        # insert a tuple containing the list element
        # the index it came from
        # the index of the value from the list itself
        minheap.insert((lists[0], i, 0))

    while minheap.get_size():
        # extract the smallest value from the heap
        minimum = minheap.delete()

        # take the next element from the same list
        # that we removed from

        # also, check if we aren't at the end of that list
        if minimum[2] + 1 < len(lists[minimum[1]]):
            next_idx = minimum[2] + 1
            replacement = lists(minimum[1][next_idx])
            next_value = (replacement, minimum[1], next_idx)
            minheap.insert(next_value)
