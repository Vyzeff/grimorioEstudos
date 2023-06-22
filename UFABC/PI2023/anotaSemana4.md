# PI - Semana 4

*   Módulo
*   Módulo `math` e `random`

## Módulo

As funções que utilizamos até agora, tais como `abs()` (valor absoluto) e `pow()` (exponenciação), fazem parte das chamadas [funções embutidas](https://docs.python.org/pt-br/3/library/functions.html) da linguagem Python.

Podemos ampliar a quantidade de funções disponíveis em um programa para além das funções embutidas. Isso pode ser feito através da **importação de módulos**.

Um módulo é um programa em Python, isto é, um arquivo em formato de texto simples com extensão `.py`. Todos os programas que escrevemos até agora são módulos.

Suponha que escrevemos um módulo `somasub.py` contendo a definição de algumas funções como a seguir:

`somasub.py`:

```python
"""Funções de soma e subtração"""

def soma(a, b):
    """Retorna a + b"""
    return a + b

def subtracao(a, b):
    """Retorna a - b"""
    return a - b

def subtracao2(a, b):
    """Faz a mesma coisa que subtracao, mas de um jeito diferente"""
    return a + (-b)
```

Em outro programa/módulo, escrevemos o seguinte:

`programa.py`:

```python
salario = 5000
bonus = 2000
despesas = 4000

receita = soma(salario, bonus)
saldo = subtracao(receita, despesas)

print("O saldo é: ", saldo)
```

Infelizmente, este último programa não funciona pois as funções `soma()` e `subtracao()` não estão definidas em `programa.py`. Podemos reescrevê-las em `programa.py`, mas isso seria reinventar a roda. Uma forma mais simples é **importar o módulo** `somasub` dentro do módulo `programa`:

`programa.py`:

```python
import somasub # <-- Importando o módulo somasub

salario = 5000
bonus = 2000
despesas = 4000

receita = somasub.soma(salario, bonus)        # <- Prefixo somasub
saldo = somasub.subtracao(receita, despesas)  # <- Prefixo somasub

print("O saldo é: ", saldo)
```

Com `import somasub`, todas as funções definidas em `somasub.py` podem ser acessadas em `programa.py`, desde que prefixadas com `somasub.`.

> Ao importar um módulo `A` dentro de um módulo `B`, todos os objetos de `A` (funções, variáveis, etc) ficam disponíveis em `B` através do prefixo `A.`.

Às vezes queremos importar apenas algumas funções do módulo, e não o módulo inteiro. Podemos fazer isso da seguinte forma:

`programa.py`:

```python
from somasub import soma, subtracao # <-- Importando as funções soma e subtracao

salario = 5000
bonus = 2000
despesas = 4000

receita = soma(salario, bonus)
saldo = subtracao(receita, despesas)

print("O saldo é: ", saldo)
```

Neste caso, importamos apenas as funções `soma()` e `subtracao()` do módulo `somasub`. A função `subtracao2()` não foi importada e por isso não está disponível em `programa.py`.

Quando usamos a forma `from <módulo> import <função1>, <função2>, ...`, não precisamos mais usar o prefixo do módulo para acessar as funções mencionadas.

Para importar todas as funções de um módulo sem precisar usar o prefixo do módulo, pode-se fazer assim:

`programa.py`:

```python
from somasub import * # <-- Importando tudo (não recomendado)

salario = 5000
bonus = 2000
despesas = 4000

receita = soma(salario, bonus)
saldo = subtracao(receita, despesas)

print("O saldo é: ", saldo)
```

Neste caso, a função `subtracao2()` também fica disponível em `programa.py`. Essa forma de importação com o `*` não é recomendada. A mistura de nomes de um módulo em outro de forma indiscriminada pode resultar em conflitos de nomes.

## Módulo `math`

O módulo `math` fornece funções matemáticas. Veja a seguir algumas das funções e variáveis disponíveis:

Função/variável | Descrição | Exemplo
:-----          | :-------  | :-------
`pi`            | Constante $\pi$ | `pi` é `3.141592...`
`e`             | Constante $e$ | `e` é `2.718281...`
`inf`           | Infinito positivo | `10**10000 < inf` é `True`
`floor(x)`      | Maior inteiro menor que `x` (*função piso*) | `floor(2.9)` é `2`
`ceil(x)`       | Menor inteiro maior que `x` (*função teto*) | `ceil(3.01)` é `4`
`sqrt(x)`       | Raiz quadrada de `x` | `sqrt(9)` é `3.0`
`exp(x)`        | $e^x$ | `exp(1)` é igual à constante `e`
`log(x)`        | Logaritmo natural de `x` | `log(e)` é `1`
`cos(x)`        | Cosseno de `x` em radianos | `cos(pi/2)` é `0`
`sin(x)`        | Seno de `x` em radianos | `sin(pi)` é `0`
`tan(x)`        | Tangente de `x` em radianos | `tan(pi/4)` é `1`

Para ver todas as funções e variáveis disponíveis em `math`, consulte a [documentação](https://docs.python.org/pt-br/3/library/math.html).

## Módulo `random`

O módulo `random` fornece funções relacionadas ao sorteio de números (geração de números pseudo-aleatórios). Algumas funções de `random` são dadas a seguir:

Função            | Descrição | Exemplo
:-----            | :-------  | :-------
`randint(a, b)`   | `int` aleatório no intervalo `[a, b]` | `randint(1, 6)`
`random()`        | `float` aleatório no intervalo `[0, 1)` | `random()`
`randrange(a, b)` | `int` aleatório no intervalo `[a, b)` | `randrange(0, 5)`
`seed(a)` | Inicializa o gerador de números usando a semente `a` (o padrão é a hora atual do sistema) | `seed(100)`

Para ver todas as funções e variáveis disponíveis em `random`, consulte a [documentação](https://docs.python.org/pt-br/3/library/random.html).

> **Exercício 4.1 - Cara ou coroa**
>
> Faça um programa que pede para o usuário adivinhar o lançamento de uma moeda. O programa deve simular o lançamento da moeda e então imprimir uma mensagem na tela informando se o usuário acertou ou não.
>
> Exemplos de execução:
>
>     Cara (0) ou coroa (1)? 0
>     Errou!
>     Foi sorteado 1 (COROA).
>      
>     Cara (0) ou coroa (1)? 1
>     Acertou!
>     Foi sorteado 1 (COROA).
>      
>     Cara (0) ou coroa (1)? 1
>     Errou!
>     Foi sorteado 0 (CARA).
>
> ***

> **Exercício 4.2 - Número palíndromo**
>
> Faça uma função `palindromo` que recebe um número inteiro positivo e retorna `True` se o número é um *palíndromo*, ou `False` caso contrário.
>
> Um número é um palíndromo se os seus dígitos, quando lidos da esquerda à direita, são iguais aos dígitos quando lidos da direita à esquerda, até o dígito central.
>
> Exemplos:
>
> *   `palindromo(123321)` é `True`.
> *   `palindromo(1234321)` é `True`.
> *   `palindromo(7)` é `True`.
> *   `palindromo(44)` é `True`.
> *   `palindromo(123)` é `False`.
> *   `palindromo(537)` é `False`.
> *   `palindromo(73865837)` é `False`.
>
> ***

> **Exercício 4.3 - Adivinhe o número**
>
> Faça um programa que pede para o usuário adivinhar um número sorteado de 1 a 100. O usuário deve ter 5 chances para acertar o número. A cada tentativa errada, o programa deve informar se o número sorteado é maior ou menor que a última tentativa.
>
> Veja os exemplos de execução:
>
>     Adivinhe o número de 1 a 100
>     Tentativas restantes: 5
>     Qual é o número: 50
>     Errou. O número sorteado é MENOR que 50
>     Tentativas restantes: 4
>     Qual é o número: 25
>     Errou. O número sorteado é MAIOR que 25
>     Tentativas restantes: 3
>     Qual é o número: 37
>     Errou. O número sorteado é MAIOR que 37
>     Tentativas restantes: 2
>     Qual é o número: 44
>     Errou. O número sorteado é MENOR que 44
>     Tentativas restantes: 1
>     Qual é o número: 40
>     Errou. O número sorteado é MAIOR que 40
>     Acabaram suas tentativas.
>     O número sorteado era 43
>
> <!---->
>
>     Adivinhe o número de 1 a 100
>     Tentativas restantes: 5
>     Qual é o número: 23
>     Errou. O número sorteado é MENOR que 23
>     Tentativas restantes: 4
>     Qual é o número: 12
>     Parabéns! Você acertou.
>     O número sorteado era 12
>
> ***

> **Exercício 4.4 - Monte Carlo**
>
> Faça uma função `pi_mc(n)` que retorna o valor aproximado de $\pi$ calculado através de `n` iterações de uma aproximação de Monte Carlo.
>
> A aproximição de $\pi$ usando Monte Carlo pode ser feita como a seguir:
>
> 1.  Sorteie $n$ pontos $(x,y)$ no plano cartesiano, onde $x$ e $y$ estão no intervalo $[0, 1)$.
> 2.  Verifique quantos desses pontos estão dentro do círculo de raio 1 ($r=1$) e centralizado na origem. Seja $m$ tal número.
> 3.  O valor aproximado de $\pi$ é $$\pi=4\frac{m}{n}$$
>
> Explicação:
> 1. A área de um círculo de raio $r$ é $$A_c = \pi r^2$$
> 2. A área de um quadrado de lado $l$ é $$A_q = l^2$$
> 3. Se o círculo está inscrito no quadrado, então $$A_q = l^2 = (2r)^2 = 4r^2$$
> 4. A razão entre as áreas do círculo e do quadrado é $$\frac{A_c}{A_q}=\frac{\pi r^2}{4r^2}$$
> 5. Agora podemos isolando o $\pi$, obtendo $$\pi = 4\frac{A_c}{A_q}$$
> 6. O método de Monte Carlo aproxima a razão entre as áreas: $$\frac{m}{n}\sim \frac{A_c}{A_q}$$
> 7. Isso é possível pois a chance de cada ponto aleatório cair dentro do círculo é proporcional à área do círculo.
> ***

> **Exercício 4.5 - Máximo divisor comum**
>
> Faça uma função que recebe dois números inteiros positivos e retorna o máximo divisor comum (MDC) entre eles. O módulo `math` possui a função `gcd()` que já faz isso. Faça o seu próprio algoritmo sem usar essa função.
>
> O MDC entre dois números pode ser calculado pelo algoritmo de Euclides. Para fazer essa conta no papel, os passos são os seguintes:
>
> 1. Escreva os números nas colunas de uma tabela em ordem decrescente:
>
> ```
> 320 | 250
> ```
>
> 2. Divida o primeiro número (320) pelo segundo (250).
> 3. Coloque parte inteira da divisão (1) sobre o número 250.
> 4. Coloque o resto da divisão (70) abaixo do número 320.
>
> ```
>     |   1
> 320 | 250
>  70 |
> ```
>
> 5. Copie o resto da divisão para a terceira coluna da segunda linha.
>
> ```
>     |   1 |
> 320 | 250 | 70
>  70 |     |
> ```
>
> 6. Repita o processo a partir do passo 2, considerando o resto como segundo número, e o primeiro como o antigo segundo número.
> 7. Termine quando o resto da divisão for igual a zero. Neste caso, o MDC é o número que está na última coluna da segunda linha.
>
> ```
>     |   1 |  3 |  1 |  1 |   3
> 320 | 250 | 70 | 40 | 30 | *10*
>  70 |  40 | 30 | 10 |  0 |
> ```
>
> 8. Logo, o MDC de 320 e 250 é 10.
> ***

> **Exercício 4.6 - Tabuleiro de xadrez**
>
> Faça uma função `xadrez(n)` que recebe um inteiro `n` positivo e imprime na tela um padrão de `n` por `n` caracteres de modo a formar um "tabuleiro de xadrez". Use `-`(hífen) e `#` (cerquilha) para denotar as casas brancas e pretas, respectivamente.
>
> Exemplos de execução:
>
> Para `xadrez(8)`:
> ```
> -#-#-#-#
> #-#-#-#-
> -#-#-#-#
> #-#-#-#-
> -#-#-#-#
> #-#-#-#-
> -#-#-#-#
> #-#-#-#-
> ```
>
> Para `xadrez(3)`:
> ```
> -#-
> #-#
> -#-
> ```
> ***

> **Exercício 4.7 - Tabuleiro de xadrez 2**
>
> A partir do programa anterior, faça uma função `xadrez2(n, x)`, onde `n` define o tamanho do tabuleiro e `x` define o tamanho de cada casa do tabuleiro.
>
> Exemplos de execução:
>
> Para `xadrez(2,3)`:
> ```
> ---###
> ---###
> ---###
> ###---
> ###---
> ###---
> ```
>
> Para `xadrez(3,5)`:
> ```
> -----#####-----
> -----#####-----
> -----#####-----
> -----#####-----
> -----#####-----
> #####-----#####
> #####-----#####
> #####-----#####
> #####-----#####
> #####-----#####
> -----#####-----
> -----#####-----
> -----#####-----
> -----#####-----
> -----#####-----
> ```
> ***