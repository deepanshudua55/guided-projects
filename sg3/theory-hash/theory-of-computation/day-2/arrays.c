#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

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

void arr_append(Array *arr, char *element)
{

    // Resize the array if the number of elements is over capacity
    // or throw an error if resize isn't implemented yet.
    if (arr->capacity <= arr->count)
    {
        fprintf(stderr, "Array at capacity.");
    }

    // Copy the element and add it to the end of the array
    // char *element_copy = malloc(sizeof(element));
    // element_copy = strcpy(element_copy,element);
    char *element_copy = strdup(element);
    arr->elements[arr->count] = element_copy;

    // Increment count by 1
    arr->count++;
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