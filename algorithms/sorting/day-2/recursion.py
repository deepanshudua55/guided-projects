# What is recursion?
# When code calls itself

# def func():
#     return func()

# In recursion there are two cases
# Base case - what makes your recursion stop
# Recursive case - what your recursive function actually does


# O(2n + 1) -> O(2n) -> O(n)
def count_down(n):
    n = n * 2
    while n >= 0:
        # print n
        print(n)
        # decrement
        n -= 1


# What is the maximum amount of times this function runs?
def count_down_recursive(n):
    print(n)
    # base case
    # what makes our recursion stop
    if n <= 0:
        return
    # recursive case
    # decrement
    return count_down_recursive(n - 1)


# print("while loop")
# count_down(10)
# print("recursive")
# count_down_recursive(10)

# What is the maximum amount of times this function runs?

# O(2^n)

# for every time that this is called, two more function calls are generated

# n = 2 = O(4)
# n = 2 = O(4)
# n = 3 = O(8)
# n = 4 = O(16)
# n = 5 = O(32)


def nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


print(nth_fibonacci(10))
