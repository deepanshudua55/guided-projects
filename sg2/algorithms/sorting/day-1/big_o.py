import math

# Big O

# What is the maximum amount of times that this loop will run?

# O(sqrt(n))


def foo(n):
    # takes the square root of n
    sq_root = int(math.sqrt(n))  # O(1)
    # runs from 0 to the square root of n
    for i in range(0, sq_root):  # runs n^.5 times
        print(i)  # O(1)


foo(4)  # runs sqrt(4) times -> runs 2 times

# O(n^2)


def bar(n):
    s = 0

    for i in range(n):         # runs n times
        for j in range(n):       # runs n times
            s += i * j             # total n * n times, or n^2 times

    return s

#  O(n sqrt(n))

# O(1) * O(x) * O(1) = O(1 * x * 1) == O(x)


def bar(x):
    sum = 0
    for i in range(0, 1463):  # somewhere between O(1463) and O(2)
        i += sum
        for j in range(0, x):      # O(x)
            for k in range(x, x + 15):   # O(15) == O(1)
                sum += 1


# O(n / 2) -> O(.5n) -> O(n)


def baz_two(array):
    print(array[0])

    midpoint = len(array) // 2

    for i in range(0, midpoint):
        print(array[i])

    # overtakes the calculation with small n, but we only care about big ns
    for _ in range(1000):
        print("hi")
