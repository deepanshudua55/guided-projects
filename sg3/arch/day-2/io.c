#include <stdio.h>
#include <stdlib.h>

// argc - argument count
// argv - array of strings - each individual commandline argument
int main(int argc, char *argv[])
{

    /*  
    open a file
    print the contents of each of its lines
    */
    FILE *fp;
    char line[1024];

    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./a.out filename\n");
        return 1;
    }

    fp = fopen(argv[1], "r");

    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file %s\n", argv[1]);
        return 2;
    }

    while (fgets(line, sizeof line, fp) != NULL)
    {
        char *endptr;
        unsigned char val = strtoul(line, &endptr, 2);

        // check if no numbers were found
        if (line == endptr)
        {
            printf("SKIPPING %s", line);
            continue;
        }

        printf("%02x\n", val);
    }

    printf("\n");
    fclose(fp);

    return 0;
}