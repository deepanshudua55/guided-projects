phonebook = ['a', 'b', 'c', 'd']

'd' in phonebook  # returns a boolean


# Best Case -> O(1)
# Average Case -> O(.5n) -> O(n)
# Worst Case -> O(n)
def find_name(name_to_find):
    for name in phonebook:  # O(n)
        if name == name_to_find:
            return True

    return False

# The fastest way would be with a binary search
# Binary search cuts its input in half with each iteration
# O(log n) - When we say O(log n) we mean log base 2
# Any time you're throwing away half the `n`s each step, you should think O(log n)
# One way to describe the log base 2 of something is:  what is the maximum amount of times this number can be split in half?
# To do a binary search, our input must be sorted


# How many times can we split 1024 in half?
1024
512  # 1
256  # 2
128  # 3
64  # 4
32  # 5
16  # 6
8  # 7
4  # 8
2  # 9
1  # 10


def binary_find_name(name_to_find, phonebook):
    # base case - what makes makes our recursion stop
    print(phonebook)
    if len(phonebook) == 0:
        return False

    # take the midpoint
    midpoint = len(phonebook) // 2

    # take the current value
    # equal to the index of the midpoint
    current = phonebook[midpoint]

    # if our criteria equals the current value
    # also a base case
    if name_to_find == current:
        return True

    # otherwise, compare our name to find with the current value

    # if smaller
    if name_to_find < current:
        # Search the lower half
        return binary_find_name(name_to_find, phonebook[:midpoint])

    # larger
    else:
        # Search the upper half
        return binary_find_name(name_to_find, phonebook[midpoint:])


# Iteration 1
# Manual binary search
# We want to find 1
# Take the midpoint - 5
# current = array[5] = 6
# criteria does not equal current 1 != 6
# criteria is less than current, so take the lower half
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iteration 2
# take the midpoint 5 // 2 = 2
# set current to array[2] = 1
# 1 != 3
# 1 is smaller than 3 so cut it in half again
[1, 2, 3, 4, 5]

# Iteration 3
# take the midpoint, which is 2/1 = 1 = 2
# 2 != 1
# 1 is smaller cut it in half again
[1, 2]

# Iteration 4
# take the midpoint which is 1/2 = .5 rounded down = 0
# array[0] = 1
# 1 == 1
# return true
[1]

print(binary_find_name(1, l))
