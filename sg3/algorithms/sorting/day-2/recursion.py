# Recursion
# Code that calls itself
# Base case - what makes our recursion stop
# Recursive case - what our function does
# Without a base case you get stack overflow


# O(n)
def count_down(n):
    # base case
    if n == 0:
        return
    print(n)
    # recursive case
    return count_down(n - 1)


def count_down_loop(n):
    for i in range(10, 0, -1):  # O(n)
        print(i)


def count_up(n):
    # base case
    # while n > 0: do this thing
    if n == 0:
        return
    # recursive case
    count_up(n - 1)
    print(n)

# count_up(10) -> count_up(9) -> count_up(8)...


print("our recursive function")
count_down(10)
print("our loop")
count_down_loop(10)
print("counting up now")
count_up(10)
print("here's our stack")
# A stack is LIFO - Last In First Out
stack = []

for i in range(10, 0, -1):
    stack.append(i)

for _ in range(10):
    print(stack.pop())


# O(2^n)
# For every one call of this function, two more calls are generated.
def nth_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fib(n - 1) + nth_fib(n - 2)


"""
# nth_fib(5)
# n - 1         n - 2
nth_fib(4)      
nth_fib(3)      nth_fib(3)
... 2           ... 2
... 1           ... 1
... 0           ... 0
"""

print(nth_fib(50))
