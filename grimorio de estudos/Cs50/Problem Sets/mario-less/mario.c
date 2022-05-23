#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h = 0;
    //ask for height input
    do
    {
        h = get_int("Please input the pyramid's desired height between 1 and 8: ");
        //printf("Height: %i\n", h);
    } while (h < 1 || h > 8 );

    //do pyramidwget

    //for loop for height of row
    for (int x = 0; x < h; x++)
    {
        //for loop to width
        for (int y = 0; y < h; y++)
        {
            //hashes
            if (x + y >= h - 1)
                printf("#");

            //add spaces
            else
            printf(" ");
        }
        printf("\n");
    }
}