//bmp guarda as informações e estruturas que vão ser usadas
//filter é que cuida da logica, o que vai realmente passar o filtro pelas imagens
//helpers.c tem as funções necessarias
//helpers.h vai declarar as funções
//makefile vai "juntar tudo.
//so temos que fazer o helpers.c, todo o resto ja foi feito
//basicamente, temos que fazer as funções que serao aplicadas nas imagens.

/*
AVISO
helpers.c somente roda na pasta problems/filter-less uma vez que por si só é
so um conjunto de funções. Para testar o programa, rode filter.c na pasta indicada.
*/

#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //mudar os valores de r, g ou b para que fiquem o mesmo, para um grayscale
    //calcular a media dos valores de 0 a 255 das cores, esse sera o valor em cinza
    //lembre de usar round

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int pixelSum = round((image[x][y].rgbtBlue + image[x][y].rgbtRed + image[x][y].rgbtGreen)  / 3.0);
            image[x][y].rgbtBlue = image[x][y].rgbtGreen = image[x][y].rgbtRed = pixelSum;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //for each pixel ---> originalPixel * sepiaPixel, if > 255 ---> 255


    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int sepiaRed = round(.393 * image[x][y].rgbtRed + .769 * image[x][y].rgbtGreen + .189 * image[x][y].rgbtBlue);
            int sepiaGreen = round(.349 * image[x][y].rgbtRed + .686 * image[x][y].rgbtGreen + .168 * image[x][y].rgbtBlue);
            int sepiaBlue = round(.272 * image[x][y].rgbtRed + .534 * image[x][y].rgbtGreen + .131 * image[x][y].rgbtBlue);
           //check if bigger than 255
           //redundante mas nao sei como fazer melhor??
            if (sepiaRed < 256)
            {
                image[x][y].rgbtRed = sepiaRed;
            }
            else
            {
                image[x][y].rgbtRed = 255;
            }
            if (sepiaGreen < 256)
            {
                image[x][y].rgbtGreen = sepiaGreen;
            }
            else
            {
                image[x][y].rgbtGreen = 255;
            }
            if (sepiaBlue < 256)
            {
                image[x][y].rgbtBlue = sepiaBlue;
            }
            else
            {
                image[x][y].rgbtBlue = 255;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //a linha fica a mesma, mas os pixels dela vao para o lugar oposto
    //ja que nao mexe na cor, nao entramos em RGBTRIPLE image
    //ajuda no stack  overflow
    //reverse array
    /*void ReverseArray(int arr[], int size)
    {
        for (int i = 0; i < size/2; ++i)
        {
            int temp = arr[i];
            arr[i] = arr[size - 1 - i];
            arr[size - 1 - i] = temp;
       }
    }*/

    for (int x = 0; x < height; x++)
    {
        //se for par
        if (width % 2 == 0)
        {
            for (int y = 0; y < width / 2; y++)
            {
                RGBTRIPLE tempImage[height][width];
                tempImage[x][y] = image[x][y];
                image[x][y] = image[x][width - (y + 1)];
                image[x][width - (y + 1)] = tempImage[x][y];
            }
        }
        //se impar
        if (width % 2 != 0)
        {
            for (int y = 0; y < (width - 1) / 2; y++)
            {
                RGBTRIPLE tempImage[height][width];
                tempImage[x][y] = image[x][y];
                image[x][y] = image[x][width - (y + 1)];
                image[x][width - (y + 1)] = tempImage[x][y];
            }
        }
    }


    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //box blur
    //média do valor de todos os 9 pixels de um determinado pixel central
    //media de red, green e blue de cada um dos 9 ao total, o novo valor sendo o novo pixel
    //lembrar nem todos os pixels tem 9 ao redor.
    //lembrar duplicar imagem com newImage para que o blur fique certo
    RGBTRIPLE newImage[height][width];

    for (int x = 0; x < height; x++) //new image to work
    {
        for (int y = 0; y < width; y++)
        {
            newImage[x][y] = image[x][y];
        }
    }


    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            //defina variaveis que vao ser a soma dos valores, assim como uma contagem de pixels iterados
            float redSum = 0;
            float greenSum = 0;
            float blueSum = 0;
            int pixelCount = 0;

            for (int a = -1; a < 2; a++) //checa de -1 ate +1 para cada x, esquerda direita
            {
                for (int b = -1; b < 2; b++) //cima a baixo para cada y
                {
                    //se o pixel está no grid ao redor de image[x][y] e existe nele
                    if (x + a >= 0 && y + b >= 0 && x + a <= height - 1 && y + b <= width - 1)
                    {
                        redSum += newImage[x + a][y + b].rgbtRed;
                        blueSum += newImage[x + a][y + b].rgbtBlue;
                        greenSum += newImage[x + a][y + b].rgbtGreen;
                        pixelCount++;
                    }
                }
            }
            //tranforma a imagem original pela media dos valores por pixelCount
            image[x][y].rgbtRed = round(redSum / pixelCount);
            image[x][y].rgbtBlue = round(blueSum / pixelCount);
            image[x][y].rgbtGreen = round(greenSum / pixelCount);
        }
    }
    return;
}
