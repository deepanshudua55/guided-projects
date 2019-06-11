#include <stdio.h>
#include <string.h>
#include <stdlib.h> // <-- include this for free and malloc

// passing an integer by reference
// and modifying it directly
void halve(int *p)
{
    *p /= 2;
}

void arr(void)
{
    // arrays must contain all of the same type of element
    // arrays can't be resized without making a new array
    // we use squirrely braces to initialize arrays
    int a[5] = {11,
                22,
                33,
                44,
                55};
    int *p = &a[0];
    // int *p = a;
    *p = 99;
    printf("the zeroth element %d\n", *(a));
    // printf("the first element %d\n", *(a + 1));
    // printf("the first element %d\n", a[1]);
    printf("the element at the second index %d\n", a[2]);
    *(p + 2) = 88;
    printf("the element at the second index %d\n", a[2]);
}

// 198 p
// 199
// 200 h -- our malloc'd space starts here
// 201 e
// 202 l
// 203 l
// 204 o
// 205 \0
// 206

void store_string(void)
{
    char *p;

    p = malloc(6); // store 6 bytes in memory
    // \0 <-- null terminating character
    strcpy(p, "hello");

    free(p);
}

int *make12(void)
{
    // allocate enough memory to store one int
    int *p = malloc(sizeof(int));

    *p = 12;

    return p;
}

void free12(int *p)
{
    free(p);
}

int main(void)
{
    // int x = 12;

    // // p is empty and doesn't point to anything
    // int *p;
    // // char *string = "hello";

    // // set p to the address of x
    // p = &x;

    // *p = 4;

    // // we're passing the address in memory
    // // that p points to
    // // halve(p);
    // // halve(&x);

    // arr();
    // printf("the address p points to: %d\n", p);
    // printf("the value p points to: %d\n", *p);
    // printf("%d\n", *p);

    int *x;

    x = make12();

    printf("the value of what x is pointing to is %d\n", *x);

    free12(x);

    return 0;
}