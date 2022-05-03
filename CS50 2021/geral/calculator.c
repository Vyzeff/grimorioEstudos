// #include <cs50.h> // tem que ser instalado por fora para contar como uma biblioteca valida(acho)
#include <stdio.h>

int main(void) {
    long x = get_long("x: ");
    long y = get_long("y: ");
    printf("%li/n", x + y);
}