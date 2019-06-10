#include <stdio.h>
#include <string.h>

void print_string(void)
{
    // create a string
    char *c = "Hello longer";

    // print out the string
    printf("Address of the c pointer: %p\n", c);
    printf("Value stored at the address: %c\n", *c);
    printf("Sizeof c %lu\n", sizeof(c));
    printf("Sizeof char %lu\n", sizeof(char));

    for (int i = 0; i < strlen(c); i++)
    {
        printf("Address: %p | Value: %c\n", c + i, *(c + i));
        printf("Address: %p | Value: %c\n", c + i, c[i]);
    }
}

void double_pointer(void)
{
    // an array containing two elements
    // an array of strings is actually an array of arrays
    char *array_of_strings[2];
    array_of_strings[0] = "first";
    array_of_strings[1] = "second";

    char *array_of_strings_two[] = {"first",
                                    "second"};
}

// this function takes in a value
// and modifies it directly
// it's passed by reference, not by value
void make99(int *p)
{
    *p = 99;
}

int main(void)
{
    // uninitialized so it has a garbage value
    int x;
    // p is a pointer to an integer
    int *p = &x;

    // now x is equal to 12
    x = 12;

    printf("p is %p\n", p);

    printf("x is %d\n", x);
    printf("p is %d\n", *p);

    // // set what p is pointing to equal to 99
    // *p = 99;
    // // identical to above
    // x = 99;
    // make99(&x);

    make99(p);

    // we expect x to be equal to 99
    printf("x is %d\n", x);
    printf("p is %d\n", *p);

    // print_string();

    return 0;
}