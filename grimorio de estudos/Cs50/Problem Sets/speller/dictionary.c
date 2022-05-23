// Implements a dictionary's functionality

#include <stdbool.h>
#include "dictionary.h"
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//output when a word from the dicionary or input is passed through hash()
unsigned int hashOutput;

//word count, to be printed at end
unsigned int wordsDictionary;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //case insensitive, strcasecmp
    //somente true se for alfabetico, com um apostrofo talvez, e se estiver no dicionario
    int wordHash = hash(word); //pega o numero do array table no qual a palavra aponta
    node *arrow = table[wordHash]; //cria uma seta
    while (arrow != NULL) //enquanto nao for a ultima palavra
    {
        if (strcasecmp(word, arrow->word) == 0) //se forem iguais, a palavra do input e a palavra que a seta aponta
        {
            return true;
        }
        arrow = arrow->next; //aponta para a proxima seta, que estava junto com a palavra
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word) //hash com base em sdbm de http://www.cse.yorku.ca/~oz/hash.html
{
    unsigned long hash = 0;
    int c;

    while ((c = tolower(*word++)))
    {
        hash = c + (hash << 6) + (hash << 16) - hash;
    }
        return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *openFile = fopen(dictionary, "r"); //abre os dicionarios dados
    if (openFile == NULL) //se foi possivel abrir, isto é, se openFile não for "nada"
    {
        return false;
    }

    char buffer[LENGTH + 1]; //um buffer onde o fscan ira guardar o que ele ler
    while (fscanf(openFile, "%s", buffer) == 1) // fscan em um %s normal retorna 1, 0 ao null e -1 ao EOF
        {
            node *n = malloc(sizeof(node));

            if (n == NULL) // malloc null == sem memória no pc, PARA
            {
                return false;
            }

            strcpy(n->word, buffer); //copia a palavra atual de buffer para n.word
            hashOutput = hash(buffer); //passa a palavra por hash()
            n->next = table[hashOutput]; //aponta para a nossa hash table
            table[hashOutput] = n; //para não ter memory leaks???
            wordsDictionary++; //conta +1 palavra por loop
        }

    fclose(openFile); //fecha para não ter memoria desperdiçada com um arquivo aberto sem uso
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (wordsDictionary > 0)
    {
        return wordsDictionary;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int x = 0; x < N; x++)
    {
        node *arrow = table[x];
        while (arrow)
        {
            node *temp = arrow;
            arrow = arrow->next;
            free(temp);
        }
        if (x == N - 1 && arrow == NULL)
        {
            return true;
        }
    }
    return false;
}
