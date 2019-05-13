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
        return f'Title: {self.title}\nAuthor: {self.author}\n Genre: {self.genre}'


unsorted = [14, 4, 11, 8, 7, 1, 9, 19, 13,
            17, 5, 3, 16, 18, 2, 20, 10, 15, 6, 12]

"""
Insertion Sort is an in-place algorithm, meaning that it does not require any additional memory to perform the sort operation.

It works by conceptually dividing the array into sorted and unsorted pieces.
Consider element at index 0 to be our sorted piece. The rest of the array is our unsorted piece.
Save the 1st element in the unsorted piece in a temp variable.
Shift elements in the sorted piece over to the right until we find where the element from step 2 should go.
Insert the element from step 2 into its correct index within the sorted piece.
Repeat steps 2-4 until all elements have been processed.
"""

# We want to sort our books in ascending order by genre


books = [
    Book('harry Potter', 'jkrowling', 'magic'),
    Book('Moby Dick', 'Herman Melville', 'fiction'),
    Book("Awesome Book", "Awesome Dude", "Romance"),
    Book("Dirk Gently's Holistic Detective Agency",
         "Adams, Douglas", "non-fiction")]

# Best case O(n) - already sorted array
# O(n^2) - on average
# Worst case - O(n^2) - elements from largest to smallest, if we want to sort in ascending order
def insertion_sort(books):
    # loop through from the first index to the last
    for i in range(1, len(books)):
        # Save the 1st element in the unsorted piece in a temp variable.
        temp = books[i]
        j = i
        # Shift elements in the sorted piece over to the right until we find where the element from step 2 should go.
        while j > 0 and temp.genre.lower() < books[j - 1].genre.lower():
            # shift left until the correct genre is found
            books[j] = books[j - 1]
            j -= 1
        books[j] = temp
    return books


print(insertion_sort(books))
