class Book:
    # books have a title, author and genre
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    # string representation of our book class
    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Genre: {self.genre}'


"""
Insertion Sort is an in-place algorithm, meaning that it does not require any additional memory to perform the sort operation
It works by conceptually dividing the array into sorted and unsorted pieces.
Consider element at index 0 to be our sorted piece. The rest of the array is our unsorted piece.
Save the 1st element in the unsorted piece in a temp variable.
Shift elements in the sorted piece over to the right until we find where the element from step 2 should go.
Insert the element from step 2 into its correct index within the sorted piece.
Repeat steps 2-4 until all elements have been processed.
"""

l = [12, 19, 7, 8, 17, 9, 7, 4, 7, 8, 5, 16, 6, 12, 7, 8, 8, 20, 3, 11]


def insertion_sort(array):
    # create loop that goes from the 1st index to last
    for i in range(1, len(array)):
        print(array)
        #  Consider element at index 0 to be our sorted piece. The rest of the array is our unsorted piece.
        # Save the 1st element in the unsorted piece in a temp variable.
        temp = array[i]
        # iterator for second loop
        # j will count downward
        j = i
        # while j is greater than 0 and our temp variable is smaller
        while j > 0 and temp < array[j - 1]:
            # Shift elements in the sorted piece over to the right until we find where the element from step 2 should go.
            # shift left until correct position is found
            array[j] = array[j - 1]
            # increment down
            j -= 1
        # Insert the element from step 2 into its correct index within the sorted piece.
        array[j] = temp
        # Repeat steps 2-4 until all elements have been processed.
    return array


print(insertion_sort(l))


def insertion_sort_books_by_genre(books):
    # create loop that goes from the 1st index to last
    for i in range(1, len(books)):
        # Save the 1st element in the unsorted piece in a temp variable.
        temp = books[i]
        j = i
        while j > 0 and temp.genre < books[j-1].genre:
            # shift left until we find where the book should go
            books[j] = books[j - 1]
            j -= 1
        # insert at the correct position
        books[j] = temp

    return books


b = Book('a', 'b', 'c')
b2 = Book('d', 'e', 'f')
b3 = Book('x', 'y', 'z')
b4 = Book('n', 'm', 'o')

books = [b4, b2, b3, b]

# print(insertion_sort_books_by_genre(books))
