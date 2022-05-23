#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>


int alphaVerify(string text);
int keyLength;
string key;
const string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


int main(int argc, string argv[])
{
    key = argv[1];
    keyLength = strlen(argv[1]);
    //verifying steps
    //verifies number of arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key. Please input only single line arguments.\n");
        return 1;
    }
    //verifies length
    else if (keyLength != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    //verifies if key is composed of letters
    else if (alphaVerify(key) != 26)
    {
        printf("Please use only letters and only one of each.\n");
        return 1;
       }
    //verification complete

    //substitution
    //calls for text input
    //ask for plainText
    string plainText = get_string("plaintext: ");
    int textLength = strlen(plainText);
    char cipherText[textLength + 1];

    //convert to cipherText
    //loop through each letter in plainText
    for (int x = 0; x < textLength; x++)
    {
        //check if uppercase and use standard alphabet/key
        if (isupper(plainText[x]) != 0)
        {
            for (int y = 0; y < keyLength; y++)
            {
                if (plainText[x] == alphabet[y])
                {
                    cipherText[x] = key[y];
                    break;
                }
            }
        }
        //if lowercase use lowercase alphabet and key
        else if (islower(plainText[x]) != 0)
        {
            for (int y = 0; y < strlen(alphabet); y++)
            {
                if (plainText[x] == tolower(alphabet[y]))
                {
                    cipherText[x] = tolower(key[y]);
                    break;
                }
            }
        }
        //non letters
        else
        {
            cipherText[x] = plainText[x];
        }
    }
    //add null char to make it a string
    cipherText[textLength] = '\0';
    //print result and exit
    printf("ciphertext: %s\n", cipherText);
    return 0;

}

//Function that actually verifies
int alphaVerify(string text)
{
    int alphaNumber = 0;
    for (int x = 0; x < keyLength; x++)
    {
        //if the character is alphabetical, proceed
        if (isalpha(key[x]) != 0)
        {
            //convert key to uppercase
            if (key[x] >= 'a' && key[x] <= 'z')
            {
                key[x] = toupper(key[x]);
            }
            //add to alphaNumber, if at the end the total sum is 26, proceed
            alphaNumber++;
            //check for repeated letters, if so, take from alphaNumber
            for (int r = x + 1; r < keyLength; r++)
            {
                if (key[x] == key[r])
                {
                    alphaNumber--;
                    return 3;
                }
            }

        }
    }
    return alphaNumber;
}
