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

int main(int argc, char *argv[])
{

    Array *arr = create_array(5);

    arr->elements[0] = "STRING1";
    arr->elements[1] = "STRING2";

    return 0;
}