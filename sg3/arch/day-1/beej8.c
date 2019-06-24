#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*  
we're creating a program that reads instructions and values
from memory and runs in a loop to execute those instructions
*/

#define PRINT_BEEJ 1
#define HALT 2
#define PRINT_NUM 3
#define PRINT_SUM 4
#define SAVE 5
#define PRINT_REGISTER 6
#define ADD 7

unsigned char memory[] = {
    PRINT_BEEJ,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT};

unsigned char registers[8];

int main(void)
{
    int cur_index = 0;
    bool running = true;

    unsigned char reg_num, val;
    unsigned char reg_num0, reg_num1;

    // while our computer is running
    while (running)
    {
        // the current command that is being executed
        unsigned char command = memory[cur_index];

        switch (command)
        {
        case ADD:
            reg_num0 = memory[cur_index + 1];
            reg_num1 = memory[cur_index + 2];

            registers[reg_num0] += registers[cur_index + 2];

            cur_index += 3;
            break;
        case SAVE:
            val = memory[cur_index + 1];
            reg_num = memory[cur_index + 2];
            registers[reg_num] = val;

            cur_index += 3;
            break;

        case PRINT_REGISTER:
            printf("%d\n", registers[memory[cur_index + 1]]);

            cur_index += 2;
            break;
        case PRINT_BEEJ:
            printf("Beej\n");
            cur_index++;
            break;
        case PRINT_NUM:
            // look ahead to the next index and print it
            printf("%d\n", memory[cur_index + 1]);
            cur_index += 2;
            break;
        case PRINT_SUM:
            // look ahead to the next index and print it
            printf("%d\n", memory[cur_index + 1] + memory[cur_index + 2]);
            cur_index += 3;
            break;
        case HALT:
            running = false;
            cur_index++;
            break;
        default:
            fprintf(stderr, "Unrecognized instruction\n");
            exit(1);
            break;
        }
    }

    return 0;
}