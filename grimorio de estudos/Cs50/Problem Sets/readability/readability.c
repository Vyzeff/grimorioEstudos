#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>



//this was much better compared to the first problem set
int main(void)
{
    //calls user input and finds length
    string input = get_string("Please, input your text here: ");
    int n = strlen(input);

    int letters = 0;
    int words = 1;
    int sentences = 0;

    //counting
    for (int i = 0; i < n; i++)
    {
            //counts letters with ASCII
            if ((input[i] >= 'a' && input[i] <= 'z') || (input[i] >= 'A' && input[i] <= 'Z'))
            {
                letters++;
            }
            //counts words with space
            else if (input[i] == ' ')
            {
                words++;
            }
            //counts sentences just like letters, with ASCII
            else if (input[i] ==  '!' || input[i] ==  '.' || input[i] ==  '?')
            {
                sentences++;
            }
        }

    //print results
    printf("%i letters\n", letters);
    printf("%i words\n", words);
    printf("%i sentences\n", sentences);

    //calculation and rounding
    float L = ((float)letters / (float)words) * 100;
    float S = ((float)sentences / (float)words) * 100;
    float calculation = 0.0588 * L - 0.296 * S - 15.8;
    int index = round(calculation);

    //print grade
     if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}