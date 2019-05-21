from dll import DoublyLinkedList # <-- this import is not checked into git, so this file will break

""" 
What sort of operations do we need be able to perform with a text editor?
- Insertion 
    - prepend - add to the front
    - append - add to the back
- Deletion - from the front and the back
- Copy/pasting

Ideally we want O(1) time complexity for every operation.
- An array wouldn't work. O(n) for prepending and deleting from the front.
- Linked List sounds good.
    - Probably a doubly linked list.

Text Buffer 1
head of buffer 1 --> h -- e -- l -- l -- o -- " " <-- tail of buffer 1

Text Buffer 2
head of buffer 2 --> w -- o -- r -- l -- d <-- tail of buffer 2

Steps to join them
1. Set the next property on the tail of buffer 1 to be the head of buffer 2.
2. set the tail of buffer 2 to be the new tail of buffer 1.
"""


class TextBuffer:
    def __init__(self, initial_text=None):
        # the contents of our buffer are stored as a linked list
        self.contents = DoublyLinkedList()
        """  
         if we are passed in initial text as an argument
         loop through the string and make linked list nodes
         with every letter 
         """
        if initial_text:
            for char in initial_text:
                self.contents.add_to_tail(char)
        # print the contents of our text buffer
    # O(n)
    def __str__(self):
        s = ""
        """ 
            loop through the linked list
            add each letter to the string
            """
        current = self.contents.head
        while current:
                # concatenate the current letter with the string
            s += current.value
            # move to the next item in the list
            current = current.next
        # __str__ must return a string
        return s

    def append(self, string_to_add):
        """  
        loop through the string
        add each char to the tail
        """
        for char in string_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, string_to_add):
        """ 
        reverse the incoming string
        then loop through it
        and add each char to the head
        """
        for char in string_to_add[::-1]:
            self.contents.add_to_head(char)

    def delete_front(self, chars_to_remove):
        """  
        takes in an argument for how many chars to delete from the front
        """
        for _ in range(chars_to_remove):
            self.contents.remove_from_head()

    def delete_back(self, chars_to_remove):
        """  
        takes in an argument for how many chars to delete from the back
        """
        for _ in range(chars_to_remove):
            self.contents.remove_from_tail()

    """  
    Joins another buffer to itself
    The tail of the current buffer will be the tail of other_buffer
    The head of other_buffer will become the head of this buffer
    """

    def join(self, other_buffer):
        # make sure other_buffer is a TextBuffer
        if not isinstance(other_buffer, TextBuffer):
            print("Join only accepts TextBuffers")
            return
        # set the the current tail to be the tail of the other buffer
        self.contents.tail.next = other_buffer.contents.head
        # set the prev property on other_buffer's head to be the tail
        other_buffer.contents.head.prev = self.contents.tail
        # set the other buffers head to be the current buffer's
        other_buffer.contents.head = self.contents.head
        # set the tail of the current buffer to be other_buffer's tail
        self.contents.tail = other_buffer.contents.tail

    """  
    takes in a string
    creates a new text buffer out of that string
    then calls self.join
    """
    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)


text = TextBuffer("hello")
# world = TextBuffer("world!")
print(text)
text.append("wo")
print(text)
text.prepend("why ")
print(text)
text.delete_front(4)
print(text)
text.delete_back(3)
print(text)
text.join_string("world!")
print(text)
