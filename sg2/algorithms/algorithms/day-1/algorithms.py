# temperature = 350
# golden_brown = False
# while not golden_brown:
#     cook_in_oven(350)

# a number multiplied by every number before it
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!


def factorial(n):
    # nth factorial is equal to the factorial of n-1
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_while(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


# given a value a and an exponent b, compute the value of a^b


def power(a, b):
    if type(b) != int:
        print("Invalid input.")
        return
    # store the original number
    multiplicant = a
    if b == 0:
        return 1
    # for loop
    elif b > 0:
        for i in range(b - 1):
            a *= multiplicant
    else:
        for i in range(b, 1, 1):
            a /= multiplicant
    print(a)


# power(2, 3)  # 8
# power(2, -3)  # .125


def nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


# nth_fibonacci(500) <- won't ever finish running because nth_fibonacci is too slow

# 5

# return nth_fibonacci(4) + nth_fibonacci(3)

# 4
#    nth_fibonacci(3) + nth_fibonacci(2)

# 3
# nth_fibonacci(2) + nth_fibonacci(1)

# 2
# nth_fibonacci(1) + nth_fibonacci(0)

# O(n + n^2) -> O(n^2)
def func(n):
    # O(n)
    for i in range(n):
        pass
    # O(n^2)
    for j in range(n):
        for k in range(n):
            pass
