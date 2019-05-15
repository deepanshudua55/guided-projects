# Turn the oven on at 350 and cook until golden brown.
# temperature = 350
# golden_brown =  False

# while not golden_brown:
#     cook_in_oven(temperature)
# house_robber
# You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.
# ​
# Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm

# Input:
# nums: [1, 1, 1]
# Expected Output:
# 2

# Input:
# nums: [1, 7, 9, 4]
# [1, 9]
# [7, 4]
# Expected Output:
# 11

# What is the maximum sum of all of the non-adjacent elements in the array.
# keep two variables for the running total of odd and even indices
# if length is 0, return 0
# if the length is 1, return the 0th index
# loop through the array
# add all the even indices
# add all the odd [1, 7, 9, 4] -> 10, 11 -> 11 > 10 -> 11
# return the biggest of the two sums


# pass 2
# [1, 3, 1, 3, 100]
# loop through the array
# nested loop, through an array of every house thats not adjacent -> [3, 100] -> 6, 103
#  [2, 1, 2, 6, 1, 8, 10, 10] 26 2 + 6 + 8 + 10
# [1, 2] ->


# def house_robber(houses):
#     # keep two variables for the running total of odd and even indices
#     odd_sum = 0
#     even_sum = 0
#     # if length is 0, return 0
#     if not len(houses):
#         return 0
#     # if length is 1, return the element
#     if len(houses) == 1:
#         return houses[0]
#     if len(houses) == 2:
#         return max(houses)

# calculate the maximum stolen value

def house_robber(arr):
    incl = 0
    excl = 0

    for i in arr:

        # Current max excluding i
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return (excl if excl > incl else incl)

# return a to the power of b

# What kind of input can we expect?
# Not use math.pow or **

# Write out the steps in pseudocode
# 2^3 = 2*2*2
# A good situation for recursion
# power(2,3)


def power(a, b):
    # base case
    if b <= 0:
        return 1
    return a * power(a, b-1)


def power_loop(a, b):
    multiplier = a
    for _ in range(b-1):
        a *= multiplier
    return a

# Evaluate
# Need to handle negative exponents


# def power_second_pass(a, b):
#     # base case
#     if b <= 0:
#         return 1
#     elif b > 0:
#         return a * power(a, b-1)
#     else:
#         return 1 / (a * power_second_pass(a, b+1))


def power_loop_second_pass(a, b):
    if b < 0:
        b = b * -1
        pow = a
        for _ in range(b-1):
            a *= pow
        return 1/a
    else:
        pow = a
        for _ in range(b-1):
            a *= pow
        return a

# Third pass - handle decimals


# def power_second_pass(a, b):
#     # base case
#     if type(b) is not int:
#         print("The exponent must be an integer")
#     if b == 0:
#         return 1
#     elif b > 0:
#         return a * power_second_pass(a, b-1)
#     else:
#         return 1 / (a * power_second_pass(a, b+1))


def rec_power(a, b):
    # Base case:
    # Anything raised to the power of 0 = 1
    if b == 0:
        return 1

    # Recursive case, POSITIVE exponent
    # Call function on `b-1`
    elif b > 0:
        return a * rec_power(a, b-1)

    # Recursive case, NEGATIVE exponent
    # Call function on `b+1`
    else:
        return 1 / (a * rec_power(a, b+1))


# call_stack = [
#     power(2, 3),  # -> 8
#     power(2, 2),  # -> 4
#     power(2, 1),  # -> 2
#     power(2, 0)  # -> 1
# ]
"""
The order that things happen:
    power(2, 0)  # -> 1
    power(2, 1),  # -> 2
    power(2, 2),  # -> 4
    power(2, 3),  # -> 8
"""

print(power(2, 3))
print(power_loop(2, 3))
print(rec_power(5, -3))
print(power_loop_second_pass(5, -3))
