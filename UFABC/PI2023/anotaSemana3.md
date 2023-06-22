# PI - Semana 3

*   Estruturas de repetição

***

## Estruturas de repetição

Estruturas de repetição, ou **laços** (em inglês, *loops*), são estruturas de código utilizadas para repetir a execução de um conjunto de instruções.

Há dois tipos de laços:

*   **Laços contáveis**:

    São utilizados quando sabemos previamente o número de vezes que o código deve ser repetido. Por exemplo, podemos pedir para o usuário digitar um inteiro `n` e então repetir um trecho de código `n` vezes.

    Em Python, um laço contável é construído com a palavra reservada `for` (para).

*   **Laços condicionais**:

    São utilizados quando não sabemos de antemão o número de repetições. Um laço condicional repete um trecho de código **enquanto uma condição lógica for verdadeira**. Por exemplo. podemos usar um laço condicional para pedir repetidamente para o usuário digitar notas e só parar quando o usuário digitar um número negativo. Nesse caso, a condição para o laço continuar é `n >= 0`, onde `n` é o último número digitado pelo usuário.

    Em Python, um laço condicional é construído com a palavra `while` (enquanto).

> Observação: quando nos referimos a estruturas de repetição, é mais comum usarmos o verbo "iterar" do que "repetir". Cada repetição de um laço é chamada de iteração.

Tanto nos laços `for` quanto nos laços `while`, podemos forçar a saída do laço com o comando `break`. Também é possível pular para a próxima iteração antes da iteração atual terminar. Isso é feito com o comando `continue`. Veremos cada um desses comandos com mais detalhes.

## `for`

Considere o programa a seguir:

```python
n = int(input("Digite um número: "))

for i in range(n):
    print(f"Iteração nº {i}")

print("Fim do programa")
```

Se o usuário digitar `5`, a saída será:

    Digite um número: 5
    Iteração nº 0
    Iteração nº 1
    Iteração nº 2
    Iteração nº 3
    Iteração nº 4
    Fim do programa

Observe que:

*   As instruções que são repetidas são aquelas que estão identadas em relação ao `for` (dizemos que elas estão "dentro" do `for` ou no escopo do `for`).
*   As instruções dentro do `for` são executadas `n` vezes, em sequência.
*   Para cada iteração, `i` contém um valor inteiro que varia de `0` a `n-1`.
*   Após todas as iterações, o fluxo de execução continua no escopo anterior.

`range(n)` é uma função embutida do Python que retorna uma sequência de inteiros de `0` a `n-1`. Para cada iteração, a variável definida após o `for` (variável `i` no exemplo anterior) contém um valor da sequência do `range`.

É comum programadores usarem a expressão "o laço itera sobre a sequência de `0` a `n-1`" para dizerem que o laço visita cada elemento da sequência durante as iterações.

A sintaxe geral do `for` é

    for <variavel> in <sequencia>:
        <instrucoes>
        ...

onde `<variavel>` é o nome da variável que assumirá cada valor da sequência, e `<sequencia>` é uma sequência de números -- como aquela retornada pela função `range` -- ou outra coleção de objetos iteráveis que veremos em aulas futuras.

Além de `range(n)`, podemos usar a sintaxe `range(inicio, fim)` para retornar uma sequência de inteiros no intervalo `[inicio, fim)` (isto é, o o intervalo é fechado em `inicio` e aberto em `fim`). Veja um exemplo:

```python
for i in range(10, 15):
    print(i)
```

Saída:

    10
    11
    12
    13
    14

Outra possível sintaxe para o `range` é `range(inicio, fim, passo)`, onde `passo` é um inteiro que corresponde ao "tamanho do passo".

O tamanho do passo é a diferença entre dois números consecutivos da sequência. Veja um exemplo com um tamanho de passo `2`:

```python
for i in range(-6, 6, 2):
    print(i)    
```

Saída:

    -6
    -4
    -2
    0
    2
    4

O tamanho do passo também pode ser negativo. Dessa forma podemos fazer uma contagem regressiva:

```python
for i in range(5, 0, -1):
    print(i)  
```

Saída:

    5
    4
    3
    2
    1

Note que, na contagem regressiva, `inicio` precisa ser maior que `fim`. Note também que o último elemento da sequência (`fim`) nunca é atingido, pois o intervalo sempre é aberto no final.

### Laços aninhados

Podemos colocar um `for` dentro de outro `for` para formar um "laço aninhado". Isso é bastante útil para visitar elementos de estruturas de dados bidimensionais, como matrizes e tabelas 2D.

O exemplo a seguir desenha um padrão de 4x6 asteriscos na tela:

```python
for i in range(4):
    for j in range(6):
        print("*", end="")
    print()
```

Saída:

    ******
    ******
    ******
    ******

> Observação: o `end=""` é utilizado para que o `print` não adicione uma nova linha após a exibição de cada asterisco.

Naturalmente, dentro do `for` também podemos colocar estruturas de decisão e quaisquer outros comandos e expressões que vimos até agora.

## `while`

Considere o programa a seguir:

```python
n = int(input("Digite um número positivo: "))

d = 0

while n > 0:
    d += 1
    n = n // 10

print(f"O número tem {d} digitos")
```

Se o usuário digitar `849`, a saída será a seguinte:

    O número tem 3 dígitos

Observe como funciona este laço `while`:

*   Na primeira vez que a linha `while n > 0:` é executada, `n` vale `849`. Como `n > 0` é `True`, o escopo do `while` é executado (**1ª iteração**).
*   Após a execução da última instrução do escopo do `while`, o fluxo do programa volta para a linha `while n > 0` para avaliar novamente a expressão `n > 0`.
*   Agora, `n` vale `84`. Como `n > 0` ainda é `True`, o escopo do `while` é executado mais uma vez (**2ª iteração**). Após isso, o fluxo do programa volta para a linha do `while`.
*   Agora, `n` vale `8`. Como `n > 0` ainda é `True`, o escopo do `while` é executado mais uma vez (**3ª iteração**). Após isso, o fluxo do programa volta para a linha do `while`.
*   Agora, `n` vale `0`. Como `n > 0` é `False`, o escopo do `while` é ignorado e a execução do programa continua na linha do `print`.

A sintaxe geral do laço `while` é

    while <expressao>:
        <instrucoes>
        ...

onde `<expressao>` é qualquer expressão cujo resultado possa ser convertido em `bool`, e `<instrucoes>` é o conjunto de instruções que serão executadas se `<expressão>` for equivalente a `True`.

> **Exercício 3.1 - Transformando `for` em `while`**
>
> No código a seguir, substitua o laço `for` por um laço `while`, sem alterar a saída do programa:
>
> ```python
> n = int(input("Digite o n: "))
>
> for i in range(n):
>    print(i)
> ```
>
> ***

> **Exercício 3.2 - Laço aninhado**
>
> O código a seguir é o mesmo do exemplo que já tínhamos visto sobre laços aninhados:
>
> ```python
> for i in range(4):
>    for j in range(6):
>        print("*", end="")
>    print()
> ```
>
> 1.  Substitua o `4` e o `6` por um valor digitado pelo usuário (número de linhas e número de colunas).
> 2.  Imprima cerquilhas (`#`) nas linhas ímpares, e asteriscos (`*`) nas linhas pares.
>
> Exemplo:
>
>     Número de linhas: 4
>     Número de colunas: 6
>     ******
>     ######
>     ******
>     ######
>
> ***

## `break`

Podemos usar a palavra `break` para sair imediatamente de um laço `for` ou `while`.

No exemplo a seguir, o `break` é utilizado para sair do laço assim que o usuário digitar a string `"sair"`:

```python
while True:
    entrada = input("Digite um número, ou 'sair': ")
    if entrada == "sair":
        break
    par_impar = "ímpar" if int(entrada) % 2 else "par"
    print(f"{entrada} é um número {par_impar}")

print("Fim do programa")
```

Exemplo de saída:

    Digite um número, ou 'sair': 10
    10 é um número par
    Digite um número, ou 'sair': 3
    3 é um número ímpar
    Digite um número, ou 'sair': 2
    2 é um número par
    Digite um número, ou 'sair': sair
    Fim do programa

Após o `break`, o fluxo de execução do programa continua no escopo imediatamente anterior ao do laço que contém o `break`.

> **Observação**
>
> No exemplo anterior, a condição do `while` é `True`. Isso significa que o laço itera indefinidamente e só termina quando o `break` é executado. Sem o `break`, teríamos um **loop infinito**. Tome cuidado para não criar loops infinitos pois eles podem travar o programa.
>
> Se o seu programa entrar em loop infinito, pressione <kbd>Ctrl+C</kbd> para forçar a interrupção.

> **Exercício 3.3 - Evitando loop infinito**
>
> O programa a seguir pede para o usuário digitar um número `n` e então faz uma contagem regressiva de `n` a `1`. Entretanto, dependendo do número digitado, o programa pode entrar em loop infinito. Identifique esse caso e modifique o programa para evitar que ele ocorra:
>
> ```python
> n = int(input("Digite o n: "))
>
> while n != 0:
>    print(n)
>    n -= 1
> ```
>
> ***

## `continue`

Dentro de um laço, podemos usar a palavra `continue` para pular imediatamente para a próxima iteração. Ao fazer isso, as instruções que ainda faltam para a execução da iteração atual são ignoradas.

O programa a seguir usa um laço `while` para pedir cinco números para o usuário. Veja como o `continue` é utilizado para ignorar a execução do resto das instruções quando `n` está fora do intervalo `[1,3]`.

```python
contador = 0

while contador < 5:
    n = int(input("Digite um número entre 1 e 3: "))

    if n < 1 or n > 3:
        print("Entrada inválida")
        continue

    if n == 1:
        print("Um")
    elif n == 2:
        print("Dois")
    else:
        print("Três")

    contador += 1
```

Exemplo de saída:

    Digite um número entre 1 e 3: 1
    Um
    Digite um número entre 1 e 3: 3
    Três
    Digite um número entre 1 e 3: 2
    Dois
    Digite um número entre 1 e 3: 5
    Entrada inválida
    Digite um número entre 1 e 3: 6
    Entrada inválida
    Digite um número entre 1 e 3: -1
    Entrada inválida
    Digite um número entre 1 e 3: 1
    Um
    Digite um número entre 1 e 3: 2
    Dois

> **Exercício 3.4 - Potência usando multiplicações**
>
> Faça um programa que pede ao usuário um número `b` (um `float`) e um `n` (um `int` não-negativo), e então imprime na tela o resultado de `b` elevado a `n` usando multiplicações (o programa não deve usar `**` ou `pow()`).
>
> Exemplos de execução:
>
>     Digite a base: 2
>     Digite o expoente: 3
>     2.0^3 = 8.0
>
>     Digite a base: 3
>     Digite o expoente: 0
>     3.0^0 = 1
>
>     Digite a base: -3
>     Digite o expoente: 3
>     -3.0^3 = -27.0
>
> ***

> **Exercício 3.5 - Potência com expoente negativo**
>
> Adapte o programa anterior para permitir expoentes negativos.
>
> Exemplos de execução:
>
>     Digite a base: 2
>     Digite o expoente: -1
>     2.0^-1 = 0.5
>      
>     Digite a base: 2
>     Digite o expoente: -2
>     2.0^-2 = 0.25
>      
>     Digite a base: -3
>     Digite o expoente: -3
>     -3.0^-3 = -0.037037037037037035
>
> ***

> **Exercício 3.6 - Soma de série**
>
> Faça um programa que pede para o usuário um inteiro `n` positivo e, usando laços, calcule a série
> $$S(n) = \frac{1}{1} + \frac{1}{3} + \dots + \frac{1}{2n+1}$$
>
> Mostre o resultado com duas casas decimais.
>
> Exemplos de execução:
>
>     Digite o n: 0
>     S(0) = 1.00
>      
>     Digite o n: 1
>     S(1) = 1.33
>      
>     Digite o n: 2
>     S(2) = 1.53
>      
>     Digite o n: 3
>     S(3) = 1.68
>      
>     Digite o n: 4
>     S(4) = 1.79
>
> ***

> **Exercício 3.7 - Fatorial**
>
> O fatorial de um inteiro $n$ não-negativo, denotado por $n!$, e é igual ao produto
> $$n! = n \times (n-1) \times (n-2) \times \cdots \times 3 \times 2 \times 1$$
>
> O fatorial de $0$ é definido como $1$, isto é,
> $$0! = 1$$
>
> Faça uma função `fatorial(n)` que retorna o fatorial de `n`. Utilize um laço para calcular o produto dos termos.
>
> Veja o fatorial de alguns números:
>
>
> $n$  | $n!$
> :--- | :---
> 0    | 1
> 1    | 1
> 2    | 2
> 3    | 6
> 4    | 24
> 5    | 120
> 6    | 720
> 7    | 5040
>
> ***

> **Exercício 3.8 - Número de Euler**
>
> A constante $e=2,71828\dots$ (número de Euler) pode ser calculada através da série
> $$e=\sum_{n=0}^{\infty}\frac{1}{n!} = 1 + \frac{1}{1} + \frac{1}{1 \cdot 2} + \frac{1}{1 \cdot 2 \cdot 3} + \cdots $$
>
> Faça um programa que pede o usuário um inteiro `n` não-negativo e calcula o número de Euler aproximado pelos termos da série de `n=0` até o `n` informado pelo usuário.
>
> Exemplos de execução:
>
>     Digite o n: 0
>     1
>     
>     Digite o n: 1
>     2.0
>     
>     Digite o n: 2
>     2.5
>     
>     Digite o n: 3
>     2.6666666666666665
>     
>     Digite o n: 4
>     2.708333333333333
>     
>     Digite o n: 5
>     2.7166666666666663
>     
>     Digite o n: 10
>     2.7182818011463845
>
> ***

> **Exercício 3.9 - Coeficiente binomial**
>
> O coeficiente binomial de um número $n$ na classe $k$ é o número de combinações de $n$ termos quando agrupados $k$ a $k$.
>
> Por exemplo, a combinação de 4 termos, agrupados 2 a 2, é 6. Se os termos são `a`, `b`, `c`, `d`, as combinações são `ab`, `ac`, `ad`, `bc`, `bd`, `cd`.
>
>O coeficiente binomial de $n$ na classe $k$ pode ser escrito como:
>
> $$\binom{n}{k}=\frac{n!}{k!(n-k)!}=\frac{n(n-1)(n-2)\cdots(n-k+1)}{k!}$$
>
> Faça uma função `binomial(n, k)` que calcula o coeficiente binomial de um número `n` na classe `k`.
>
> Exemplos:
>
> * `binomial(4, 2)` é `6`.
> * `binomial(0, 0)` é `1`.
> * `binomial(10, 0)` é `1`.
> * `binomial(6, 4)` é `15`.
> * `binomial(60, 6)` é `50063860` (número de combinações da Mega-Sena).
>
> ***

> **Exercício 3.10 - Triângulo de Pascal**
>
> Faça um programa que pede para o usuário um inteiro `n` positivo e então imprime na tela as `n` primeiras linhas do "triângulo de Pascal".
>
> Como calcular o triângulo de Pascal:
>
> *   O primeiro elemento de cada linha do triângulo de Pascal é sempre 1.
> *   O elemento $P_j$ ($j>1$) da linha $i$ do triângulo de Pascal é dado por
>     $$P_j = \frac{P_{j-1}[i-(j-1)]}{j-1}$$
>
> Exemplo de execução:
>
>     Número de linhas: 6
>     1 
>     1 1 
>     1 2 1 
>     1 3 3 1 
>     1 4 6 4 1 
>     1 5 10 10 5 1 
>
> O triângulo de Pascal está relacionado com o coeficiente binomial. O valor na linha $n$ e coluna $k$ do triângulo -- supondo que $n$ e $k$ iniciem em zero -- é 
> $$\binom{n}{k}$$
>
> ***

> **Exercício 3.11 - FizzBuzz**
>
> Faça um programa que pede para o usuário um inteiro `n` positivo e então imprime na tela os números de 1 a `n`, um por linha. Entretanto, considere que 
>
> * se o número for divisível por 3, o programa deve imprimir a palavra `"Fizz"` no lugar do número;
> * se o número for divisível por 5, deve imprimir a palavra `"Buzz"`;
> * se o número for divisível por 3 e 5 ao mesmo tempo, deve imprimir a palavra `"FizzBuzz"`.
>
> Exemplo de execução:
>
>     Digite o n: 15
>     1
>     2
>     Fizz
>     4
>     Buzz
>     Fizz
>     7
>     8
>     Fizz
>     Buzz
>     11
>     Fizz
>     13
>     14
>     FizzBuzz
>
> ***

> **Exercício 3.12 - Fibonacci**
>
> Faça um programa que pede para o usuário um inteiro `n` positivo e então imprime na tela os `n` primeiros termos da _sequência de Fibonacci_. Use laços para fazer o algoritmo.
>
> A sequência de Fibonacci é a sequência na qual cada número é a soma dos dois últimos números, sendo que os dois primeiros números da sequência são 0 e 1:
>
> `0`, `1`, `1`, `2`, `3`, `5`, `8`, `13`, `21`, `34`, `55`, `89`, `144`, ...
>
> Exemplo de execução:
>
>     Digite o n: 8
>     0
>     1
>     1
>     2
>     3
>     5
>     8
>     13
>
> ***