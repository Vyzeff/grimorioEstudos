#include <cs50.h>
#include <stdio.h>

//it was really hard to wrap my head around this, is this really the first problem set?
int main(void){

    //number input
    long creditNumber = get_long("Please input your credit card number: ");
    printf("Credit Number: %.0li\n", creditNumber);

    //check number length
    int length = 0;
    long n = creditNumber;

    while (n > 0)
    {
        n = n / 10;
        length++;
    }
    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }clear


    //calculate the sum
    int firstSum = 0;
    int secondSum = 0;
    long x = creditNumber;
    int total = 0;
    int mod1;
    int mod2;
    int d1;
    int d2;
    do
    {
        // Remove last digit and add to firstSum
        mod1 = x % 10;
        x = x / 10;
        firstSum = firstSum + mod1;

        // Remove second last digit
        mod2 = x % 10;
        x = x / 10;

        // Double second last digit and add digits to secondSum
        mod2 = mod2 * 2;
        d1 = mod2 % 10;
        d2 = mod2 / 10;
        secondSum = secondSum + d1 + d2;

    }
    while (x > 0);
    total = firstSum + secondSum;
    //next check Luhn Algorithm
    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    //get starting digits
    long start = creditNumber;
    do
    {
        start = start / 10;
    }
    while (start > 100);
    //check starting digits for card type
    //mastercard
    if ((start / 10 == 5) && (0 < start % 10 && start % 10 < 6))
    {
        printf("MASTERCARD\n");
    }
    else if ((start / 10 == 3) && (start % 10 == 4 || start % 10 == 7))
    {
        printf("AMEX\n");
    }
    else if (start / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
