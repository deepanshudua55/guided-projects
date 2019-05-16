import random
import operator
from time import time

"""
PROBLEM: Given a text file, words.txt, print out the largest set of anagrams.
rasp -> spar
a signature is all the letters of a word in sorted order

the signature of rasp and spar: aprs
1. Understand
What is an anagram?
anagram
a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

2. Plan 
- Generate all sets of anagrams
    - Keep a dictionary for all signatures - key is the signature and value is the number of pairs
    - Make it lowercase
    - Sort the word
    - Check if its in the dictionary
    - Put the signature into a dictionary if it isn't, otherwise increment the signature
- Find the biggest
"""

# 3. Implement

# O(n * k)


def first_pass_anagrams(words):

    # generate random values for each char a-z
    chars = [0] * 26  # O(26)
    for i in range(26):  # O(26)
        chars[i] = random.randint(0, 1000000)  # O(1)

    # create new dictionary
    anagrams = {}  # O(1)
    signature = 0  # O(1)

    # use random char values to calculate a "value" of each word
    for word in words:  # O(n)
        word = word.lower()  # O(1)
        for char in word:  # O(k)
            index = ord(char)-97
            if index >= 0 and index < 26:
                signature += chars[index]
        # groups words with same value
        if signature not in anagrams:  # O(1)
            anagrams[signature] = []
        anagrams[signature].append(word)
        signature = 0

    # get max entry in dictionary
    maxAnagrams = max(anagrams.items(), key=operator.itemgetter(1))[0]

    print(maxAnagrams)

# second pass

# O(n * klogk)
# k is the average length of an english word


def second_pass_anagrams(words):
    # create new dictionary
    anagrams = {}

    longest = None

    # GENERATE ALL SETS OF ANAGRAMS
    for word in words:
        # convert list to string
        signature = "".join(sorted(word.lower()))  # O(4.5 logn) -> 4.5 * 2.17
        if signature not in anagrams:
            anagrams[signature] = []
        anagrams[signature].append(word)
        # UPDATE LARGEST SET AS WE CREATE THEM
        if longest == None or len(anagrams[signature]) > len(anagrams[longest]):
            longest = signature

    print(anagrams[longest])

# third pass


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
            maxAnagrams = anagrams[signature]
    print(maxAnagrams)


f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# TEST IT!
start_time = time()
first_pass_anagrams(words)
end_time = time()
print(f"1st pass runtime: {end_time - start_time} seconds\n")

start_time = time()
second_pass_anagrams(words)
end_time = time()
print(f"2nd pass runtime: {end_time - start_time} seconds\n")


start_time = time()
third_pass_anagrams(words)
end_time = time()
print(f"3rd pass runtime: {end_time - start_time} seconds\n")
