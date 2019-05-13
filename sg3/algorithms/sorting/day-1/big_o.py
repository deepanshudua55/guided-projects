import math


# What is the maximum amount of times this function runs?

# O(1) + O(sqrt(n))
# Reduces to O(sqrt(n))
# This function will run a maximum of sqrt(n) times
def foo(n):
    sq_root = int(math.sqrt(n))  # O(1)
    for i in range(0, sq_root):  # O(sqrt(n))
        print(i)  # O(1)


foo(4)


# O(n * n) or O(1 + n^2 + 1)
# reduce to O(n^2)
def bar(n):
    sum_of_multiplying = 0  # O(1)

    for i in range(n):  # O(n) - this loop will run n times
        for j in range(n):  # O(n) - this loop will run n times
            sum_of_multiplying += i * j  # O(1)

    return sum_of_multiplying  # O(1)


# O(1 + n * sqrt(n) + 1) -> O(n * sqrt(n))
def baz(n):
    result = 0  # O(1)

    for i in range(n):  # O(n)
        for j in range(int(math.sqrt(n))):  # O(sqrt(n))
            result += i * j  # O(1)

    return result  # O(1)


# O(1 + 2 + n + 15) -> O(n)
def bar2(n):
    result = 0  # O(1)
    for i in range(0, 1463):  # somewhere between O(2) and O(1463)
        i += result  # O(1)
        for j in range(n):  # O(n)
            for k in range(n, n + 15):  # O(15)
                result += 1  # O(1)


# O(1 + 1 + .5n + O(1000))
# O(1 + 1 + .5n + 1)
# O(1 + 1 + n + 1)
# O(n)

def baz2(array):
    print(array[1])  # O(1)

    # if n is 7, 7 -> 3
    midpoint = len(array) // 2  # O(1)

    for i in range(0, midpoint):  # O(n/2)
        print(array[i])  # O(1)

    for _ in range(1000):  # O(1000)
        print('hi')  # O(1)
