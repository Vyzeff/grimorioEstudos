#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;


 /*
 checar o input, se for mais de 1, return 1
 se o arquivo nao puder ser aberto, return 1
abrir pasta com os dados
procurar o começo de um JPG
criar um novo JPG
continuar fazendo o JPG em blocos de 512 bytes até o inico de um novo com os mesmos bytes de começo
 */
int main(int argc, char *argv[])
{
    //check arg count
    if (argc != 2)
    {
        printf("Please, only use a single argument, ./recover filename\n");
        return 1;
    }

    //open file from input
    char *pathName = argv[1];
    FILE *inputData = fopen(pathName, "r");

    BYTE buffer[512]; //an array of 512 bytes
    char fileName[8];
    int imageCount = 0;
    int foundJpg = 0;
    FILE *outputData = NULL; //an "empty" file that will be used later

    //check if pathname valid
    if (inputData == NULL)
    {
        printf("File cannot be accessed, please try again.\n");
        return 1;
    }
    else
    {
        while (fread(buffer, 512, 1, inputData) == 1) //while there is still data to read on input,
        {                                             //read 1 chunk of 512 bytes at a time and store it on buffer
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xe0) == 0xe0)
            {
                if (foundJpg == 1)
                {
                    fclose(outputData); //close the previous file
                }
                else
                {
                    foundJpg = 1;
                }
                sprintf(fileName, "%03d.jpg", imageCount); //prints a file called ###.jpp, it is empty
                outputData = fopen(fileName, "w"); //changes the previous "empty" file to the just created jpg
                imageCount++;
            }
            if (foundJpg == 1)
            {
                fwrite(buffer, 512, 1, outputData); // on outputData, write in 1 chunks of 512 bytes from buffer.
            }
        }
    }
    fclose(outputData); //closes files to prevent memory leak
    fclose(inputData);
    return 0;
}