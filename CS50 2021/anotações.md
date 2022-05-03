

# Lesson 0 - Scratch
>What matters is not so much where you end up relative to other, but where you end up
>relative to yourself

- Computer Science == Problem solving??
    basicamente input --> output
computadores essencialmente somente se comunicam através do binário, 1 e 0.
base 2: 
    001 = 1 
    mas 010 = 2
    até 111 = 7, ad infinitun
transistores, ligado(1) ou desligado(0)

- No final do dia, a gente transforma letras e coisas que nos podemos entender em números, de uma maneira unificada. 
Exemplo, em todos os pcs do mundo, A = 01000001
diferenças no modo de como coisas são representadas, para que o numero 65(01000001) ainda seja usado e não confundido com A se dão através dos formatos de arquivos, de txt, md, até py ou exe e PNG
>computadores são muito dependentes de contexto

- Bit seria a menor unidade do computador, uma unidade de 0
    byte = 8 bits
ASCII é o modelo padrão de bits para letras, mas é preso a 255 caracteres
Unicode é uma superposição de ASCII com muito mais opções, de 8 bits do ASCII até 16 ou 32, até um máximo de 4 bilhoes de combinações 

- RGB --> mistura de red, green e blue que formam basicamente todas as cores que vemos através de pixels. 
Cada cor leva 8 bits, e pode ser contada até um máximo de 255 para uma maior intensidade, e cada pixel é uma mistura desses valores para uma definida cor.

- Um video é basicamente uma série de imagens sendo passadas muito rapido, o FPS(Frames Per Second) representa exatamente isso
Para aúdio, por meio do formato MIDI, por exemplo, representa notas músicais como números.

- Hoje em dia, para filmes e arquivos maiores, usar esse metodo de imagem por imagem seria muito díficil.
Então através de sofwares, matemática e compressão, representamos os mesmos valores de imagens, sons e mais em um tamanho menor.
Lossless =  compressão sem perda de data
lossy = compressao com alguma perda de qualidade, audio pior ou imagens pixeladas.

- Algoritmos
Passo a passos de instruções para uma finalidade
correto =! eficiente
exemplo, para achar um nome de uma letra, dividir pela metade os dados, se está na letra, antes ou depois, elimine a outra metade, repita até achar.
n = t, uma relação de 1 pra 1 para dados e esforço
n/2 = t, para cada 1 dado, .5 esforço
log2n = t, para cada log2n
quanto menor redundância, melhor

- Pseudocode
não é codigo, mas uma maneira de se expressar(linha 34)

- Abstração
classes e objetos, criar definições humanas através de codigo. Uma ação como "meow" pode ser uma função complexa, mas com um nome reconhecivel.


# Lesson 1 - C
> correctness, style, design

- IDEs
Integrated Development Environment, ou, Editores de Texto, são os "lugares" proprios para a criação de programas, uma vez que não nem o foco estético que outros aplicativos como Google Docs tem, e sim foco na funcionalidade.

- C
Um documento .c define o contexto da linguagem C
>#include <stdio.h>
>
>int main(void)
>{
>    printf("hello, world\n");
>}

- Compiler
Aquilo que realiza o processo de [sourceCode] -----> [machineCode] 

- Terminal
A janela que uma pessoa usa para interagir com o computador através do input de comandos. Exemplos são o cmd e o próprio Git.

- Funções, num geral
tem dois possiveis finais:
um efeito = algo aparece na tela, um texto, um número, som imagem, etc
um retorno = retorna um valor, uma variavel, como um resultado de pesquisa, uma solução matemática, que pode então ser reusado(como um input, onde o valor inputado fica salvo)
Em C, uma função pode ser definida como:
<void meow(void)>
isto é, uma função que não retorna nada ou um tipo de data, por isso o void no começo, e no momento ela não tem qualquer input, por isso o (void)

- #include
equivalente ao import do python, esse comando importa alguma coisa de bancos de funções.
[stdio.h] = printf e input e output num geral
[cs50.h] = algumas funções que não vem com C normalmente, como [get_string]

- Essencial para o C
Para qualquer arquivo .c, é necessário: <int main(void)>

- Floating-Point Imprecision
Fundamentalmente, computadores não são capazes de computar um numero infinito de números uma vez que tem uma capacidade finita de armazenamento e, especificamente, bits.

- Int/int
dividir um interger por um interger devolve um interger, isto é, não é possível ter números decimais num processo chamado "truncação"(truncated)


# Lesson 2 - Arrays

- Clang
ao usar $ make, não usamos o compiler por si so, mas uma ferramenta que busca ele. O compiler é chamado de Clang. Sem mais comandos, Clang não busca as bibliotecas como <stdio.h> ou <cs50.h> Serie necessário o comando -lcs50 para utilizar as funções de cs50. Make somente ajuda e deixa o processo automático. Até mesmo para nomear o arquivo seria preciso o comando -o "nome". -l significa "link"

-

# Comandos e Mais

- ./ e outros comandos
[make] = procura o compiler para um arquivo .c ou outro atualmente em uso e o compila
[.] = dentro do diretorio atual
[..] = "sobe" um diretorio do terminal
[/] = executa ou abre o arquivo nomeado
[rm] = remove um arquivo
[ls] = lista os arquivos do diretorio atual
[mv] = "move" move algum arquivo a algum diretório
[mkdir] = "make directory" cria um diretório
[cd] = "change directory" muda o diretório do terminal
[code] = cria um arquivo
[/n] = nova linha
[%s] = um placeholder para strings, como printf("Olá, %s/n", nome);
[||] = ou
[&&] = e
[printf] = equivalente ao print() do phyton

- Prefixos e mais
[bool] = true or false
[char] = um único caractére
[double] = mais precisao que float
[float] = numero real, com numero decimal
[int] = números simples
[long] = um grande int
[string] = letras e alfabeto
[+] = soma
[-] = subtrai
[/] = divide
[*] = multiplica
[%] = divite até o resto