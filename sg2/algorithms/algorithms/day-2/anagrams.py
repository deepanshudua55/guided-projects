from time import time

# PROBLEM: Given a text file, words.txt, print out the largest set of anagrams.

# an anagram is a word that's made by rearranging the letters of another word

# spar -> rasp -> pars

# s, p, a, r
# r, a, s, p

# a, p, r, s

# O(n log n)

# to check if two strings are an anagram of each other - make them lowercase, sort them, join them, then compare for equality

# makes the text file into a list
f = open('words.txt', 'r')
f = f.read().split("\n")
# f.close()

# Assigns a random numerical value to each word based on the characters it contains
# Groups words by their value
# Prints out the largest set

# O(n^2)


def first_pass_anagrams(words):
    import random
    import operator

    # generate random values for each char a-z
    chars = [0] * 26
    for i in range(26):
        chars[i] = random.randint(0, 1000000)

    # create new dictionary
    anagrams = {}
    signature = 0

    # use random char values to calculate a "value" of each word
    for word in words:
        word = word.lower()
        for char in word:
            index = ord(char)-97
            if index >= 0 and index < 26:
                signature += chars[index]
        # groups words with same value
        if signature not in anagrams:
            anagrams[signature] = []
        anagrams[signature].append(word)
        signature = 0

    # get max entry in dictionary
    maxAnagrams = max(anagrams.items(), key=operator.itemgetter(1))[0]

    print(maxAnagrams)


# O(n * n log n) -> O(n^2 * log n)

def second_pass_anagrams(words):
    # create a new dictionary
    anagrams = {}

    longest = None

    # generate all sets of anagrams
    for word in words:  # O(n)
        # convert the list to string
        signature = "".join(sorted(word.lower()))  # O(n logn)
        # add signature to our dictionary
        # dictionary has O(1) access
        if signature not in anagrams:  # O(1)
            anagrams[signature] = []  # O(1)
        anagrams[signature].append(word)  # O(1)
        # check if the list we just added to is longer than the longest
        # O(1)
        if longest is None or len(anagrams[signature]) > len(anagrams[longest]):
            # set the longest to be our signature
            longest = signature  # O(1)
    print(longest)


def third_pass_anagrams(words):
    # create new dictionary
    anagrams = {}

    # GENERATE ALL SETS OF ANAGRAMS
    for word in words:
        # convert list to string
        signature = "".join(sorted(word.lower()))
        if signature not in anagrams:
            anagrams[signature] = []
        anagrams[signature].append(word)

    # FIND LARGEST SET OF ANAGRAMS
    maxLen = 0
    maxAnagrams = []
    for signature in anagrams:
        if len(anagrams[signature]) > maxLen:
            maxLen = len(anagrams[signature])


start_time = time()
first_pass_anagrams(f)
end_time = time()
print(f'first pass time: {end_time - start_time}')
start_time = time()
second_pass_anagrams(f)
end_time = time()
print(f'second pass time: {end_time - start_time}')
start_time = time()
third_pass_anagrams(f)
end_time = time()
print(f'third pass time: {end_time - start_time}')
