from time import time
import json

# Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

"""
# Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.
For s = "CodefightsIsAwesome" and x = "IA", the output should be
strstr(s, x) = -1;
For s = "CodefightsIsAwesome" and x = "IsA", the output should be
strstr(s, x) = 10.
"""


# find out if x is in s
# does s contain a substring that matches x

# loop through s
# if we find the first letter in x - create a string slice of s after that index
# store the current index
# start our second loop and keep going through the sliced string as long as the letters match
# if we get to the end of x then return the found index
# return -1 by default


# O(???)
# first pass

"aaaaaabaaaaab"
"aaaaaak"


def strstr_fp(s, x):
    # variable for the found index
    found_idx = None
    for idx, char in enumerate(s):
        # if the char is equal to x[0]
        if char == x[0]:
            found_idx = idx
            sliced = s[idx:idx+len(x)]
            for letter_idx, letter in enumerate(sliced):
                if letter == x[letter_idx]:
                    if letter_idx == len(x) - 1:
                        return found_idx
                    else:
                        continue
                else:
                    found_idx = None
                    break
    return -1


# print(strstr_fp("CodefightsIsAwesome", "an"))
# print(strstr_fp("CodefightsIsAwesome", "IsA"))

"aaab"
"ab"

# instead of the second have an increment count for where we are in the substring

# O(n)
# second pass


def strstr(s, x):
    x_idx = 0
    found_idx = None
    for idx, char in enumerate(s):  # O(n)
        if char == x[x_idx]:
            # check if found index already exists
            if found_idx is None:
                found_idx = idx
            # increment the x_idx
            x_idx += 1
            if x_idx == len(x):
                return found_idx
        # if the current letter doesn't match up
        else:
            # reset the x index and the found index
            x_idx = 0
            found_idx = None
            # if it's the first char of x, then treat it as a match
            if char == x[0]:
                x_idx += 1
                found_idx = idx
    return -1


def strstr_ivan(s, x):
    search_word_length = len(x)
    for idx, i in enumerate(s):
        if i == x[0]:
            word = s[idx: idx+search_word_length]
            if word == x:
                return idx
    return - 1


f = open("test-21.json", 'r')
text_input = json.load(f)['input']
s_string = text_input['s']
x_string = text_input['x']
s = s_string
x = x_string

print("First Pass Solution")
start_time = time()
strstr_fp(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))
print("Second pass solution")
start_time = time()
strstr(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))
print("Ivan's")
start_time = time()
strstr_ivan(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))


f = open("test-22.json", 'r')
text_input = json.load(f)['input']
s_string = text_input['s']
x_string = text_input['x']
s = s_string
x = x_string

# print("First Pass Solution")
# start_time = time()
# strstr_fp(s, x)
# end_time = time()
# print(format((end_time - start_time), "1.12f"))
print("Second pass solution")
start_time = time()
strstr(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))
print("Ivan's")
start_time = time()
strstr_ivan(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))

f = open("test-25.json", 'r')
text_input = json.load(f)['input']
s_string = text_input['s']
x_string = text_input['x']
s = s_string
x = x_string

# print("First Pass Solution")
# start_time = time()
# strstr_fp(s, x)
# end_time = time()
# print(format((end_time - start_time), "1.12f"))
print("Second pass solution")
start_time = time()
strstr(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))
print("Ivan's")
start_time = time()
strstr_ivan(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))

f = open("test-26.json", 'r')
text_input = json.load(f)['input']
s_string = text_input['s']
x_string = text_input['x']
s = s_string
x = x_string

# print("First Pass Solution")
# start_time = time()
# strstr_fp(s, x)
# end_time = time()
# print(format((end_time - start_time), "1.12f"))
print("Second pass solution")
start_time = time()
strstr(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))
print("Ivan's")
start_time = time()
strstr_ivan(s, x)
end_time = time()
print(format((end_time - start_time), "1.12f"))
