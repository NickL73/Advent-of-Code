#include <stdio.h>
#include <stddef.h>
#include <ctype.h>
#include <stdlib.h>

static int get_digits (char * p_line);

int main(int argc, char * argv[])
{
    int sum_total = 0;
    FILE * p_file = NULL;
    char * p_line = NULL;
    size_t len = 0;
    ssize_t nread = 0;

    p_file = fopen("day1.txt", "r");
    if (NULL == p_file)
    {
        return -1;
    }

    int line_total = 0;
    nread = getline(&p_line, &len, p_file);
    while (-1 != nread)
    {
        line_total = get_digits(p_line);
        if (-1 == line_total)
        {
            printf("Failed to get total from line.\n");
            return -1;
        }

        sum_total += line_total;
        nread = getline(&p_line, &len, p_file);
    }
    
    fclose(p_file);

    if (NULL != p_line)
    {
        free(p_line);
        p_line = NULL;
    }

    printf("The summed total is: %d.\n", sum_total);
    return 0;
}

static int get_digits (char * p_line)
{
    if (NULL == p_line)
    {
        return -1;
    }

    int first_digit = -1;
    int second_digit = -1;

    int index = 0;
    char cur = p_line[index];
    do
    {
        if (isdigit(cur))
        {
            if (-1 == first_digit)
            {
                first_digit = cur - '0';
            }

            else
            {
                second_digit = cur - '0';
            }
        }

        index++;
        cur = p_line[index];
    } while ('\0' != cur);

    if (-1 == first_digit)
    {
        return -1;
    }

    if (-1 == second_digit)
    {
        second_digit = first_digit;
    }

    int final = (10 * first_digit) + second_digit;
    return final;
}
