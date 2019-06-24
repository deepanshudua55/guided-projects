#include <stdio.h>
#include <stdlib.h>
// 0 1
// false true

/*  
hex
0-9
A-F
10 - A
11 - B
12 - C
13 - D
14 - E
15 - F
16 - 10

base 10 (decimal)

+-----1000's place 10^3
|+----100's place 10^2
||+---10's place 10^1
|||+--1's place 10^0
||||
abcd

1234 == (1 * 1000) + (2 * 100) + (3 * 10) + (4 * 1)

+-----8's place (0b1000's place) 2^3
|+----4's place (0b100's place) 2^2
||+---2's place (0b10's place) 2^1
|||+--1's place (0b1's place) 2^0
||||
abcd

1110 (binary)

0b1110 == (8 * 1) + (4 * 1) + (2 * 1) + (0 * 1) == 14

1100 1010
 12   10
 C    A

 0xCA

 0x73

 7     3
 0b01110011

 54 in decimal
*/

int main(void)
{
    int x = 54;

    // decimal
    // printf("%d\n", x);
    // // hex
    // printf("%x\n", x);

    char *s = "110110";

    x = strtoul(s, NULL, 2);

    // decimal
    printf("%d\n", x);
    // hex
    printf("%x\n", x);
}
