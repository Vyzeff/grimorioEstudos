#include <stdio.h>
#include <cs50.h>


int main(void)
{
    string name = get_string("How are you called? ");
    printf("Hello %s!\n", name);
}