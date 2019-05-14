# How do quicksort and mergesort get to be O(n logn)?
# with recursion
# They are divide and conquer algorithms
# What is a divide algorithm?
# 1. Divides a problem into subproblems - logn
# 2. Solves the subproblems
# 3. Combines the results of the subproblems to get the solution

# Quicksort

"""
1. Pick a pivot. Like the first or the last index.
2. a. Move all elements that are smaller to the left of the pivot.
   b. Move all elements that are larger to the right of the pivot.
3. Recursively sort the left hand side and the right hand side until a side only contains a single element <- our base case.
"""
# Space complexity
# How much more additional memory does this algorithm require as n grows?
# Uses the same Big-O notation

# O(n) space complexity
# def print_numbers(n):
#     arr = []
#     for i in range(1, n + 1):
#         arr.append(i)
#     print(arr)
"""
Using 0th index for the pivot
[5 9 3 7 2 8 1 6]
Pass 1 - [3 2 1] [5]         [9 7 8 6]

Pass 2 - [] [3] [2 1]        [7 8 6] [9] []
        
Pass 3 -  [1] [2]     [6] [7] [8]
"""


# O(1 + 1 + 1 + n - 1) -> O(n - 1) -> O(n) time complexity
# O(n) space complexity
def partition(data):
    left = []  # O(1)
    pivot = data[0]  # O(1)
    right = []  # O(1)

    for i in data[1:]:  # O(n - 1)
        if i <= pivot:  # O(1)
            left.append(i)  # O(1)
        else:
            right.append(i)  # O(1)

    return left, pivot, right


# O(n logn)
# n = 1024, O(1024 * 10 = 10, 240)
def quicksort(data):
    # base case
    if data == []:
        return data
    left, pivot, right = partition(data)  # <- O(n)
    # concatenate the LHS + pivot + RHS
    return quicksort(left) + [pivot] + quicksort(right)  # <- O(log n)


class Book:
    """ 
    title: "title"
    author: "last name, first name"
    genre: "fiction"
    """

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    # the string representation of our class in the console

    def __repr__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\n Genre: {self.genre}\n'


books = [
    Book('harry Potter', 'jkrowling', 'magic'),
    Book('Moby Dick', 'Herman Melville', 'fiction'),
    Book("Awesome Book", "Awesome Dude", "romance"),
    Book("Dirk Gently's Holistic Detective Agency",
         "Adams, Douglas", "non-fiction")]

# Use quicksort to sort our books in ascending order by genre


# O(n logn) time complexity
# O(1)
def quicksort_ip(books, low, high):
    # base case
    # this means our array only contains a single element
    if low >= high:
        return books
    # recursive case
    # divide
    # low should be 0
    pivot = low
    # loop through each element in the subarray
    # Our parition - O(n)
    for i in range(low, high + 1):
        # check if the element at index i is smaller than the pivot
        if books[i].genre < books[pivot].genre:
            # double swap to move the smaller elements to the correct index
            # move the current element to the right of the pivot
            # temp = books[pivot + 1]
            # books[pivot] = books[i]
            # books[i] = temp
            books[pivot + 1], books[i] = books[i], books[pivot + 1]

            # swap pivot with the current element - which is now on its right
            books[pivot], books[pivot + 1] = books[pivot + 1], books[pivot]
            # increment the pivot index
            pivot += 1

    # conquer
    # quicksort everything on the LHS
    books = quicksort_ip(books, low, pivot)
    # quicksort on the RHS
    # use pivot + 1 for the low because range is inclusive for the start
    books = quicksort_ip(books, pivot + 1, high)

    return books


print(quicksort_ip(books, 0, len(books) - 1))
# print(books)
