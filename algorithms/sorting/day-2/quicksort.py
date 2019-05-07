# A recursive sorting algorithm
# Divides a problem into different subproblems
# Solves subproblems
# Combines the results into a final product

# Start by chosing a pivot
# Move all elements smaller than the pivot to the left
# Move all elements larger to the right
# Recursively do quicksort and the left hand and right hand sides
# base case - if array is empty, return the array

"""
[5 9 3 7 2 8 1 6]
pick a pivot - 5
make a sublist of everything smaller to the left
make a sublist of everything larger to the right
iteration 1 - [3 2 1] [5]  [ 9 7 8 6 ]
iteration 2 - [2 1] [3] []    [7 8 6]   [9] []
iteration 3 - [1] [2] []      [6] [7] [8]
"""

unsorted = [19, 8, 7, 18, 14, 10, 1, 17, 20,
            2, 3, 5, 6, 13, 15, 4, 9, 16, 11, 12]

# divides our arrays into subarrays


def partition(data):
    left = []
    pivot = data[0]
    right = []
    # loop through everything except for the pivot
    for number in data[1:]:
        # if smaller or equal to, put in the left hand side
        if number <= pivot:
            left.append(number)
        # if larger, put in the right
        else:
            right.append(number)
    return left, pivot, right

# does the actual sorting


def quicksort(data):
    # base case
    if len(data) == 0:
        return data
    # divde up our array
    left, pivot, right = partition(data)
    # recursive case
    # create a concentated array from the LHS, pivot and RHS
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(unsorted))

# O(n) space complexity


def new_list(n):
    my_new_list = []
    for i in range(n):
        new_list.append(i)
    return my_new_list


# In place quicksort for a bookshelf


class Book:
    # books have a title, author and genre
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    # string representation of our book class
    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Genre: {self.genre}'


b = Book('a', 'b', 'c')
b2 = Book('d', 'e', 'f')
b3 = Book('x', 'y', 'z')
b4 = Book('n', 'm', 'o')

books = [b4, b2, b3, b]

# in place is preferred because it doesn't require any new memory

# takes in our list of books
# low is the lowest index
# high is the highest index


def quicksort_ip(books, low, high):
    # base case
    if low >= high:
        return books
    else:
        # divide
        pivot = low
        for i in range(low, high + 1):
            # divide everything into the LHS and RHS
            if books[i].genre < books[pivot].genre:
                # move the current element to the right of the pivot
                temp = books[pivot + 1]
                books[pivot + 1] = books[i]
                books[i] = temp

                # swap the pivot element with the one on its right
                temp = books[pivot]
                books[pivot] = books[pivot + 1]
                books[pivot + 1] = temp
                pivot += 1

                # pivot is 19
                # compare 19 to 8
                # 8 is smaller, swap
                # [19, 8, 7] -> [8, 19 7]
        # conquer
        # sort the LHS
        books = quicksort_ip(books, low, pivot)
        # sort the RHS
        books = quicksort_ip(books, pivot + 1, high)

    return books


quicksort_ip(books, 0, len(books) - 1)

print(books)
