directions = ['n', 's', 'w', 'e']

# O(n)

# same as doing 'e' in directions


def find_letter(letter, directions):
    # loop through the directions
    for direction in directions:
        # if it is found, return True
        if direction == letter:
            return True
    # return False by default
    return False

# A binary search, with each iteration reduces the size of the array/list it's searching
# It's a divide and conquer algorithm
# This what makes it O(logn)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
     27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# O(logn)

# takes in a list of sorted items


def find_with_binary_search(criteria, array):
    # if criteria is bigger than array[-1] then return False
    if criteria > array[-1] or len(array) == 0:
        return False
    # create a base case

    # midpoint of our input array
    midpoint = len(array) // 2

    current = array[midpoint]

    if current == criteria:
        return True

    if criteria > current:
        # search the top half of the array
        return find_with_binary_search(criteria, array[midpoint:])

    if criteria < current:
        # search the bottom half of the array
        return find_with_binary_search(criteria, array[:midpoint])


print(find_with_binary_search(5, l))


# iteration 1
# take the midpoint which is 25
# set the item at the index of the midpoint to be the current value
# it's not equal to the criteria, so keep going
# check if our criteria is smaller or larger
# in this case it's smaller, so take the bottom half
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# iteration 2

# take the midpoint, 13
# set the item at the index of the midpoint to be the current value
# it's not equal to the criteria, so keep going
# compare size to our criteria - criteria is smaller again
# cut it in half and take the smaller half
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# iteration 3

# take midpoint, which is 6
# set the item at the index of the midpoint to be the current value
# it's not equal to the criteria, so keep going
# compare the size - criteria is smaller
# cut it in half and take the smaller half
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# iteration 4

# take the midpoint, which is 3
# set the item at the index of the midpoint to be the current value
# it's not equal to the criteria, so keep going
# compare the size - criteria is larger
# cut it in half and take the larger half
[1, 2, 3, 4, 5, 6]

# iteration 5

# take the midpoint, which is 5
# set the item at the index of the midpoint to be the current value
# that equals our criteria, so return it

5
