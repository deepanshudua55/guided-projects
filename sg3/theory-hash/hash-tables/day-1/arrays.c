#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>

// array of strings
typedef struct Array
{
    /*  
capacity - how many elements can this array hold?
count - how many elements does this array currently hold
elements - the contents of the array
*/
    int capacity;
    int count;
    char **elements;
} Array;

// constructor function

Array *create_array(int capacity)
{
    // malloc the size of the Array struct
    Array *arr = malloc(sizeof(Array));

    // set initial values for the capacity and count
    arr->capacity = capacity;
    arr->count = 0;

    // allocate memory for elements
    arr->elements = malloc(capacity * sizeof(char *));

    return arr;
}

/*****
 * Create a new elements array with double capacity and copy elements
 * from old to new
 *****/
void resize_array(Array *arr)
{
    arr->capacity *= 2;
    // Create a new element storage with double capacity
    // char **new_elements = malloc(arr->capacity * sizeof(char *));
    // // Copy elements into the new storage
    // for (int i = 0; i < arr->count; i++)
    // {
    //     new_elements[i] = arr->elements[i];
    // }
    arr->elements = realloc(arr->elements, sizeof(char *) * arr->capacity);
    // Free the old elements array (but NOT the strings they point to)
    // free(arr->elements);
    // // Update the elements and capacity to new values
    // arr->elements = new_elements;
}

void arr_insert(Array *arr, char *element, int index)
{

    // Throw an error if the index is greater than the current count
    if (index > arr->count)
    {
        fprintf(stderr, "IndexError: Index not found.");
    }
    // Resize the array if the number of elements is over capacity
    if (arr->count == arr->capacity)
    {
        resize_array(arr);
    }
    // Move every element after the insert index to the right one position
    for (int i = arr->count; i > index; i--)
    {
        arr->elements[i] = arr->elements[i - 1];
    }
    // Copy the element (hint: use `strdup()`) and add it to the array
    char *new_element = strdup(element);
    arr->elements[index] = new_element;
    // Increment count by 1
    arr->count++;
}

void arr_append(Array *arr, char *element)
{

    // Resize the array if the number of elements is over capacity
    // or throw an error if resize isn't implemented yet.
    if (arr->capacity <= arr->count)
    {
        resize_array(arr);
    }

    // Copy the element and add it to the end of the array
    arr_insert(arr, element, arr->count);
}

/*****
 * Remove the first occurence of the given element from the array,
 * then shift every element after that occurence to the left one slot.
 *
 * Throw an error if the value is not found.
 *****/
void arr_remove(Array *arr, char *element)
{

    // Search for the first occurence of the element and remove it.
    bool found = false;
    for (int i = 0; i < arr->count; i++)
    {
        if (found)
        {
            // Shift over every element after the removed element to the left one position
            arr->elements[i - 1] = arr->elements[i];
        }
        else if (strcmp(arr->elements[i], element) == 0)
        {
            // Don't forget to free its memory!
            free(arr->elements[i]);
            found = true;
        }
    }

    if (found)
    {
        // Decrement count by 1
        arr->count--;
        arr->elements[arr->count] = NULL;
    }
    else
    {
        fprintf(stderr, "ValueError: %s not found.", element);
    }
}

char *arr_read(Array *arr, int index)
{

    // Throw an error if the index is greater or equal to than the current count
    if (index >= arr->count)
    {
        fprintf(stderr, "IndexError: list index out of range.");
        return NULL;
    }

    // Otherwise, return the element at the given index
    return arr->elements[index];
}

/*****
 * Free memory for an array and all of its stored elements
 *****/
void destroy_array(Array *arr)
{

    // Free all elements
    for (int i = 0; i < arr->count; i++)
    {
        free(arr->elements[i]);
    }

    // Free array
    free(arr->elements);
    free(arr);
}

int main(int argc, char *argv[])
{

    Array *arr = create_array(5);
    // arr->elements[0] = "STRING1";
    // arr->elements[1] = "STRING2";
    return 0;
}