""" Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1. """

l = [2, 1, 3, 5, 3, 2]  # 3
multiple = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]  # 6
no_dups = [2, 4, 3, 5, 1]  # -1


# O(n)
def first_duplicate(arr):
    # have a set for storage
    # loop through the array
    # check if the number is in the in the set
    # if it is return the number
    # else add to the set
    cache = set()
    for num in arr:
        if num not in cache:
            cache.add(num)
        else:
            return num
    # if we get down here
    # there's no duplicates
    return -1


print(first_duplicate(l))
print(first_duplicate(multiple))
print(first_duplicate(no_dups))
