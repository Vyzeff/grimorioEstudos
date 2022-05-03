//#include <cs50.h>
#include <stdio.h>

int main(void){
    int n;
    do{
        n = get_int("Size: ");
    }
    while(n < 1);

    // for each row
    for (int i = 0, i < n, i++)
        //for each columm
        for (int j = 0, j < n, j++){
            printf("#");
    
    }
        printf("/n");
}
    
}