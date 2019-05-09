# O(2^n)

# key is the n, value is the fib number
cache = {0: 0, 1: 1}


def slow_nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

# O(n) time complexity
# O(n) space complexity
def nth_fibonacci(n):
    # check if it's in the cache
    if n in cache:
        return cache[n]
    # calculate the fib number
    result = nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    cache[n] = result
    return result

# O(n) time complexity
# O(1)/constant space complexity
def nth_fib_while(n):
    count = 1
    previous = 0
    current = 1
    while count < n:
        # add previous + current
        temp = current
        current += previous
        # set that equal to current
        # set previous equal to current's old value
        previous = temp
        # increment count
        count += 1
    return current

 # <- won't ever finish running because nth_fibonacci is too slow
print(nth_fib_while(10))

# n-1                                          # n - 2

# 5

# return nth_fibonacci(4) + nth_fibonacci(3)

# 4
#    nth_fibonacci(3) + nth_fibonacci(2)    nth_fibonacci(3) + nth_fibonacci(2)

# 3
# nth_fibonacci(2) + nth_fibonacci(1)       nth_fibonacci(2) + nth_fibonacci(1)

# 2
# nth_fibonacci(1) + nth_fibonacci(0)       nth_fibonacci(1) + nth_fibonacci(0)
