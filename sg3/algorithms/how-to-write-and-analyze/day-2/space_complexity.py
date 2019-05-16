# Time complexity
# What's the maximum amount of time a function runs?

# What's the big-O of...

# Accessing an element in array
# O(1)
l = [1]
l[0]
# Searching through an array
# O(n)

# Space complexity
# Uses the same big-O notation
# how much additional space our function needs
# Describes how the amount of memory required increases with the size of the input.

# O(n - 1) -> O(n) Time complexity
# O(n) space complexity


def partition(data):
    left = []  # O(1) - length = n/2
    pivot = data[0]  # O(1)  length = 1
    right = []  # O(1) length = n/2

    for i in data[1:]:  # O(n - 1)
        if i <= pivot:  # O(1)
            left.append(i)  # O(1)
        else:
            right.append(i)  # O(1)

    return left, pivot, right


# O(1 + .1n) -> O(.1n) -> O(n)
# O(.1n) -> O(n)
def one_tenth(n):
    # creates a new array that is .1n in size
    arr = []  # O(1)

    for i in range(n//10):  # O(.1n)
        arr.append(i)  # O(1)


# O(log n) time complexity - it splits its input in half each time
# O(n) space complexity (probably)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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


binary_find_name(1, l)


# O(n^2) time complexity
# O(1000) -> O(1) space complexity
def loop(n):
    arr = 1000 * [0]
    for i in range(n):
        for j in range(n):
            print(i*j)


# O((2 ^ n - 1) - 1)
# For every one call of this function, two more calls are generated.
def nth_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fib(n - 1) + nth_fib(n - 2)


nth_fib(5)
