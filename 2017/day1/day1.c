#include <stdlib.h>
#include <stdio.h>

static int do_part_1(FILE * p_file)
{
    if (NULL == p_file)
    {
        printf("You gave me a bad input.\n");
        return -1;
    }

    int total = 0;

    int index = 0;
    int first = 0;
    int prev = 0;
    for ( ;; )
    {
        int c = fgetc(p_file);
        if (EOF == c)
        {
            break;
        }

        if (0 == index)
        {
            first = c - '0';
        }

        if ((c - '0') == prev)
        {
            total += (c - '0');
        }

        prev = c - '0';
        index ++;

    }

    if (prev == first)
    {
        total += prev;
    }
    
    return total;
}

int main(int argc, char * argv[])
{
    int ret_val = -1;
    FILE * p_file = NULL;

    if (argc != 2)
    {
        printf("Supply a file name.\n");
        goto COMPLETE;
    }

    p_file = fopen(argv[1], "r");
    if (NULL == p_file)
    {
        printf("Could not open file.\n");
        goto COMPLETE;
    }

    int value = do_part_1(p_file);
    printf("The answer for part 1 is %d.\n", value);

    fclose(p_file);

COMPLETE:
    return ret_val;
}
