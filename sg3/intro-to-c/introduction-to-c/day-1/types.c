#include <stdio.h>
#include <stdbool.h>

// returns a boolean
// this is used in our main function
// has to be declared before main
bool return_bool(int num)
{
    if (num == 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}

int main(void)
{
    int x = 2;         // 16 bit integer
    float pi = 3.14;   // 32 bit float
    double dub = 2.55; // 64 bit float
    char c = 'c';      // character, 16 bits
    bool my_bool = return_bool(1);
    // ternary operator - is this true, if so do first, if not do second
    int n = my_bool ? 1 : 0;
    x = 3;
    // immutable
    const int unchanging = 5;
    printf("x is %d\n", x);
    printf("pi is %f", pi);
    printf("dub is %f", dub);
    printf("c is %c %%\n", c);
    int status = printf("n is %d\n", n);
    printf("status is %d\n", status);
    int d = x + 10;
    float e = pi + 10;
    int f = c + 10; // this will give 109
    float g = x + pi;
    pi = 11;
    return 0;
}
