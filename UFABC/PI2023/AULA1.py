from math import floor

def aula1(name: str, quad):
        """
        Função inicial criada durante a primeira aula.
        """

        print(f"Ola {name}!")

        if (type(quad) == int):
            ufaYear = floor(quad / 3)
            if(ufaYear > 1):
                print(f"Que bom saber que você já está no seu {ufaYear} ano na UFABC!")
            else:
                print("Bem vindo a UFABC, você ainda não completou um ano inteiro aqui, mas espero que esteja gostando daqui!")
        else:
            print(f"Que bom saber que você, {name} já está no seu {quad} quadrimestre na UFABC!")

def main():
    yourName = input("Seu nome: ")
    yourQuad = input("Seu quadrimestre atual: ")
    try:
        yourQuadNum = int(yourQuad)
        aula1(yourName, yourQuadNum)
    except:
        print("Parece que você escreveu seu quadrimestre em um não numeral! Que dificuldade.")
        aula1(yourName, yourQuad)

if "__main__" == __name__:
    main()
