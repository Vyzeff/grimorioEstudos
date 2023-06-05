# PI - Semana 2

*   Estruturas de decisão
*   Depuração

***

## Estruturas de decisão

Estruturas de decisão/seleção, também chamadas de **desvios condicionais**, são estruturas de código que permitem que um programa execute instruções distintas de acordo com o resultado de uma expressão booleana. Essa é uma forma de **tomar decisões** em um programa.

Em Python, estruturas de decisão são construídas usando as palavras-chave `if` (se), `else` (senão) e `elif` (senão se).

Veremos cada tipo de estrutura a seguir.

## `if`

Considere o seguinte código:

```python
n = int(input("Digite um número:" ))

if n == 5:
    print("Você digitou 5!")
    print("5 é meu número favorito!")

print("Obrigado. Tenha um bom dia.")
```

Neste programa, as mensagens `"Você digitou 5!"` e `"5 é meu número favorito!"` são mostradas na tela apenas se a expressão `n == 5` em `if n == 5:` for avaliada como `True`.

Se o resultado da expressão `n == 5` for `False`, as instruções que estão identadas após o `if` não são executadas.

As instruções que estão identadas após o `if` fazem parte do **escopo** do `if`.

Essa estrutura é chamada de desvio condicional porque o fluxo de execução do programa é *desviado condicionalmente* para o escopo do `if` caso a expressão após o `if` seja equivalente ao valor `True`.

## `if` ... `else` (se ... senão)

Com a estrutura `if` ... `else` podemos criar dois desvios: um para o caso `True` e outro para o caso `False`.

Considere o seguinte código:

```python
n = int(input("Digite um número: "))

if n < 0:
    print("O número é menor que zero.")
else:
    print("O número não é menor que zero.")

print(f"O número digitado é {n}")
```

Neste programa, o fluxo de execução do programa é desviado para o escopo do `if` caso `n` seja menor que zero, (isto é, se `n < 0` for avaliado como `True`). Senão, o fluxo de execução é desviado para o escopo do `else`.

## `if` ... `elif` ... `else` (se ... senão se ... senão)

Com a estrutura `if` ... `elif` ... `else` podemos criar uma sequência de desvios. O fluxo de execução é desviado para o escopo da primeira condição que tiver a expressão for avaliada como `True`. Se nenhuma expressão for avaliada como `True`, o fluxo é desviado para o escopo do `else` (se existir).

Veja o seguinte exemplo:

```python
temperatura = int(input("Temperatura do chuveiro (em °C): "))

if temperatura >= 43:
    print("Muito quente. Você pode se queimar!")
elif temperatura >= 38:
    print("Banho quente.")
elif temperatura >= 29:
    print("Banho morno.")
else:
    print("Banho frio.")

dif = abs(36.5 - temperatura)
print(f"A diferença em relação à temperatura corporal é de {dif} graus.")
```

As condições são avaliadas como a seguir:

*   Se `temperatura >= 43` for `True`, a mensagem `"Muito quente. Você pode se queimar!"` é exibida.
*   Caso contrário, se `temperatura >= 38` for `True`, a mensagem `"Banho quente."` é exibida.
*   Caso contrário, se `temperatura >= 29` for `True`, a mensagem `"Banho morno."` é exibida.
*   Caso contrário, a mensagem `"Banho frio."` é exibida.

Ao final do programa, é exibida uma mensagem informando a diferença de temperatura em relação à temperatura média do corpo.

## `if` ... `else` como expressão

Considere o seguinte exemplo:

```python
n = float(input("Digite a nota de 0 a 10: "))

if n >= 5:
    resultado = "aprovado"
else:
    resultado = "reprovado"

print(f"Você está {resultado}.")
```

É possível simplificar o desvio condicional transformando-o em uma expressão, isto é, em algo que resulte em um valor:

```python
n = float(input("Digite a nota de 0 a 10: "))

resultado = "aprovado" if n >= 5 else "reprovado"

print(f"Você está {resultado}.")
```

No código acima, a expressão no lado direito do operador de atribuição pode ser lida em português como:

O valor é `"aprovado"` se `n>=5`, senão é `"reprovado"`.

O valor resultante da expressão (`"aprovado"` ou `"reprovado"`) é então atribuído à variável `resultado`.

### Observações sobre estruturas condicionais

*   É possível criar uma estrutura condicional dentro de outra. Por exemplo, dentro do escopo de um `if` podemos escrever outro `if` (ou `if`...`else`, ou `if`...`elif`...`else`).

    Veja um exemplo:

    ```python
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    faltas = int(input("Digite o número de faltas: "))

    media = (n1 + n2) / 2

    if faltas < 7:
        if media >= 5:
            print("Aprovado")
        else:
            print("Reprovado (F)")

        print(f"A média é {media:2.f}")
    else:
        print("Reprovado por faltas (O).")

    print("Fim do programa")
    ```

    Neste exemplo, a aprovação ou reprovação por média só é verificada se o número de faltas for menor que 7.

    *   Note o uso de identação para definir quais instruções estão no escopo do segundo `if` e no escopo do `else` correspondente.
    *   Note também que, quando todas as instruções de um escopo são executadas, o fluxo de execução continua no escopo imediatamente anterior.

*   A expressão de um `if` ou `elif` pode ser qualquer expressão cujo resultado possa ser convertido em `bool`. Veja um exemplo:

    ```python
    faltas = int(input("Digite o número de faltas: "))

    if faltas:
        print("Você teve faltas.")
    else:
        print("Você não teve faltas.")
    ```

    A variável `faltas` é do tipo `int`. Durante a avaliação do `if`, o valor `int` é convertido para `bool` usando as regras que vimos na primeira semana. Logo,

    *   se o valor de `faltas` é `0`, o resultado da conversão em `bool` será `False`.
    *   se o valor de `faltas` não é `0`, o resultado da conversão em `bool` será `True`.

    Desse modo, `if faltas:` é a mesma coisa que `if faltas != 0`.

> ### **Exercício 2.1 - Maioridade e voto obrigatório**
>
> Faça um programa que pede para o usuário sua idade (valor do tipo `int`).
>
> O programa deve mostrar na tela uma mensagem dizendo se o usuário é maior ou menor de idade. Em seguida, o programa deve mostrar outra mensagem dizendo se, de acordo com as regras do Tribunal Superior Eleitoral, o voto do usuário é obrigatório, facultativo, ou se não pode votar.
>
> Lembre-se que:
>
> *   A pessoa é considerada maior de idade se tiver 18 anos ou mais.
> *   O voto é facultativo apenas para:
>     *   menores de idade a partir de 16 anos;
>     *   pessoas com 70 anos ou mais.
> *   Menores de 16 anos não podem votar.
>
> Veja alguns exemplos de execução do programa:
>
>     Qual é a sua idade? 15
>     Você é menor de idade.
>     Você ainda não pode votar.
>
>     Qual é a sua idade? 16
>     Você é menor de idade.
>     Seu voto é facultativo.
>
>     Qual é a sua idade? 40
>     Você é maior de idade.
>     Seu voto é obrigatório.
>
>     Qual é a sua idade? 70
>     Você é maior de idade.
>     Seu voto é facultativo.
>
> ***

> ### **Exercício 2.2 - Ponto no círculo**
>
> Faça um programa que determina se um ponto está dentro de um círculo. Além disso, o programa deve imprimir a distância do ponto até o centro do círculo, com duas casas decimais.
>
> A entrara do programa são 4 valores do tipo `float` digitados pelo usuário:
>
> 1.  Coordenada $x$ do ponto;
> 2.  Coordenada $y$ do ponto;
> 3.  Raio do círculo;
> 4.  Coordenada $x$ do centro do círculo;
> 5.  Coordenada $y$ do centro do círculo.
>
> Veja alguns exemplos de execução do programa:
>
>       Coordenada x do ponto: 2
>       Coordenada y do ponto: 3
>       Raio do círculo: 5
>       Coordenada x do centro do círculo: 4
>       Coordenada y do centro do círculo: 5
>       O ponto (2.0, 3.0) está DENTRO do círculo!
>       A distância até o centro do círculo é 2.83.
>
>       Coordenada x do ponto: 10
>       Coordenada y do ponto: 12
>       Raio do círculo: 10
>       Coordenada x do centro do círculo: 0
>       Coordenada y do centro do círculo: 0
>       O ponto (10.0, 12.0) está FORA do círculo!
>       A distância até o centro do círculo é 15.62.
>
> ***

> ### **Exercício 2.3 - Ano bissexto**
>
> Faça um programa que verifica se o ano informado pelo usuário é bissexto.
>
> *   São bissextos todos os anos múltiplos de 400 (ex: 1600, 1200, 2400, 2800);
> *   Também são bissextos todos os anos múltiplos de 4 que não sejam múltiplos de 100 (ex: 1996, 2004, 2008, 2012);
> *   Não são bissextos todos os demais anos.
>
> Veja alguns exemplos de execução do programa:
>
>       Qual é o ano? 2000
>       2000 é um ano bissexto.
>
>       Qual é o ano? 2024
>       2024 é um ano bissexto.
>
>       Qual é o ano? 2010
>       2010 não é um ano bissexto.
>
>       Qual é o ano? 1800
>       1800 não é um ano bissexto.
>
> ***

> ### **Exercício 2.4 - Estrela da Morte**
>
> Corre o rumor de que o Império Galáctico está construindo uma Estrela da Morte. Quando vista de longe, a Estrela da Morte tem o formato de uma circunferência com um circunferência menor dentro dela.
>
> Como combatente da Aliança Rebelde, faça um programa que identifica se duas circunferências formam uma Estrela da Morte. Duas circunferências formam uma Estrela da Morte se a circunferência menor estiver dentro da circunferência maior e, além disso, a diferença entre os raios for maior que 5.
>
> O programa deve pedir para o usuário 6 valores do tipo `float`:
>
> 1.  Coordenada $x$ do centro da circunferência 1;
> 2.  Coordenada $y$ do centro da circunferência 1;
> 3.  Raio da circunferência 1;
> 4.  Coordenada $x$ do centro da circunferência 2;
> 5.  Coordenada $y$ do centro da circunferência 2;
> 6.  Raio da circunferência 2.
>
> Veja alguns exemplos de execução do programa:
>
>       Coordenada x do centro da circunferência 1: 4
>       Coordenada y do centro da circunferência 1: 6
>       Raio da circunferência 1: 10
>       Coordenada x do centro da circunferência 2: 15
>       Coordenada y do centro da circunferência 2: 6
>       Raio da circunferência 2: 4
>       Ufa, não é uma Estrela da Morte.
>
>       Coordenada x do centro da circunferência 1: 0
>       Coordenada y do centro da circunferência 1: 0
>       Raio da circunferência 1: 9
>       Coordenada x do centro da circunferência 2: 3
>       Coordenada y do centro da circunferência 2: 6
>       Raio da circunferência 2: 3
>       Ufa, não é uma Estrela da Morte.
>
>       Coordenada x do centro da circunferência 1: 0
>       Coordenada y do centro da circunferência 1: 0
>       Raio da circunferência 1: 9
>       Coordenada x do centro da circunferência 2: 3
>       Coordenada y do centro da circunferência 2: 2
>       Raio da circunferência 2: 3
>       É uma Estrela da Morte! Chame o Luke!
>
> Que a força esteja com você!
>
> ***

## Depuração de código no VS Code

Depuração (em inglês, *debugging*) é uma técnica através da qual o programador formula hipóteses para identificar a causa de um erro em um programa, e então testa essas hipóteses através da execução do programa e/ou através da análise do código fonte.

O programa abaixo calcula o conceito na disciplina de Processamento da Informação, mas há algo de errado. Quando as notas são muito altas (por exemplo, `P1=10`, `P2=9.5` e `epsilon=0.5`), o conceito acaba sendo `F` por algum motivo misterioso. Isso também acontece quando a média é `7`.

```python
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))
epsilon = float(input("Digite o epsilon: "))

media = p1 * 0.4 + p2 * 0.6 + epsilon

if media >= 8.5 and media <= 10:
    conceito = 'A'
elif media > 7 and media < 8.5:
    conceito = 'B'
elif media >= 5.5 and media < 7:
    conceito = 'C'
elif media >= 5 and media < 5.5:
    conceito = 'D'
else:
    conceito = 'F'

print(f"O conceito final é {conceito}")
```

Podemos usar depuração para tentar descobrir a causa desses erros.

O primeiro passo da depuração é determinar os valores de entrada que reproduzem o erro. Em nosso caso já sabemos que notas muito altas dão erro, e que a média `7` também dá erro. Podemos tentar outras notas altas para ver se o problema persiste. A partir desses resultados podemos formular hipóteses sobre a causa dos erros.

Teste com:

*   `P1=9.5`, `P2=10`, `epsilon=0.5`
*   `P1=10`, `P2=10`, `epsilon=0`
*   `media=6.99`
*   `media=7.01`

Ao testar com esses valores, veremos que o erro só persiste no primeiro caso. Isso significa que o *bug* parece estar relacionado com o `epsilon` e com o fato da média ser *exatamente* `7`.

O próximo passo da depuração é analisar o código. Uma forma simples de fazer isso é através do chamado **"teste de mesa"**.

O teste de mesa consiste em executar o código mentalmente, linha por linha (instrução por instrução), escrevendo em um papel o valor de cada variável naquele momento. Através dessa análise minuciosa o programador consegue (com sorte) identificar a causa do problema.

### Depurador

**Depurador** é um programa que auxilia o programador a fazer o teste de mesa. Através do depurador é possível executar o código linha por linha e ver qual é o valor de cada variável em cada instante.

No VS Code, o depurador é iniciado pressionando <kbd>Ctrl+Shift+D</kbd> e então clicando no botão "Run and Debug" na janela do lado esquerdo. Na primeira vez que essa ação é feita é necessário selecionar o tipo de configuração de depuração. Devemos selecionar "Python File" com o arquivo Python aberto no editor.

Quando o depurador é iniciado, o programa é executado. À princípio, nada de diferente acontece. Entretanto, o programador pode usar a tecla <kbd>F9</kbd> para inserir e remover **pontos de parada** (*breakpoints*) em linhas do código. Experimente pressionar <kbd>F9</kbd> com o cursor do teclado em alguma linha de código. Você verá que aparecerá uma bolinha vermelha do lado do número da linha. Você pode inserir quantos pontos de parada quiser. Após inserir um ou mais pontos de parada, inicie o depurador novamente.

Quando uma linha com ponto de parada é alcançada durante a depuração, a execução do programa é suspensa momentaneamente antes de executar a linha em questão. O programador pode então verificar o valor das variáveis naquele momento, seja consultando a janela à esquerda, seja deixando o cursor do mouse sobre o nome da variável. Também é possível alterar o valor das variáveis na janela à esquerda.

Para continuar a execução que foi suspensa em um ponto de parada, basta pressionar <kbd>F5</kbd>. A execução continuará até o fim do programa ou até o próximo ponto de parada.

Quando um ponto de parada é atingido, também é possível continuar a executar o código linha por linha, usando <kbd>F10</kbd>.

### Teclas de atalho do depurador no VS Code

Tecla | Descrição
:---- | :-----------------------
`F9`  | Insere ou remove um ponto de parada na linha atual.
`F5`  | Continua a executar o programa até o próximo ponto de parada, ou até o fim do programa.
`F10` | Executa a linha atual.
`F11` | Executa a linha atual e, se a linha atual tiver uma chamada de função, entra nessa função.
`Shift+F11`     | Se estiver em uma função, executa o resto da função e volta para a linha que a chamou.
`Shift+F5`      | Interrompe a depuração do programa
`Ctrl+Shift+F5` | Reinicia a depuração do programa

> ### **Usando o Depurador**
>
> Insira um ponto de parada na primeira linha do programa anterior e inicie o depurador do VS Code.
>
> Durante a depuração, pressione <kbd>F10</kbd> para executar o programa linha a linha.
>
> Identifique os bugs e corrija-os.
>
> ***

> ### **Exercício 2.5 - Tipo de triângulo**
>
> Faça um programa que recebe do usuário três valores do tipo `float` e então verifica se esses valores formam os comprimentos dos lados de um triângulo. Se este for o caso, determine também se o triângulo é equilátero, isósceles ou escaleno.
>
> Para formar um triângulo:
>
> *   nenhum dos lados pode ter comprimento menor ou igual a zero;
> *   cada lado deve ser menor que a soma dos outros dois lados.
>
> Tipos de triângulo:
>
> *   Equilátero: três lados iguais;
> *   Isósceles: apenas dois lados iguais;
> *   Escaleno: três lados diferentes.
>
> Exemplos de execução do programa:
>
>       Comprimento 1: 2
>       Comprimento 2: 2
>       Comprimento 3: 5
>       Não é um triângulo
>
>       Comprimento 1: 2
>       Comprimento 2: 3
>       Comprimento 3: 4
>       Escaleno
>
>       Comprimento 1: 2
>       Comprimento 2: 2
>       Comprimento 3: 3
>       Isósceles
>
>       Comprimento 1: 2
>       Comprimento 2: 2
>       Comprimento 3: 2
>       Equilátero
>
> ***

> ### **Exercício 2.6 - Ordem crescente**
>
> Faça um programa que recebe do usuário três valores do tipo `float` e então mostra esses valores em ordem crescente.
>
> Exemplos de execução do programa:
>
>       Entre com os três números:
>       20
>       -2
>       10
>       Em ordem crescente:
>       -2.0 10.0 20.0
>
>       Entre com os três números:
>       3
>       2.1
>       -10.6
>       Em ordem crescente:
>       -10.6 2.1 3.0
>
> ***

> ### **Exercício 2.7 - Pedra, papel, tesoura**
>
> Faça um programa que simula o jogo pedra-papel-tesoura.
>
> No início o programa pede a jogada dos jogadores 1 e 2.
> As entradas possíveis são `0` (pedra), `1` (papel) e `2` (tesoura).
>
> O programa deve então verificar quem ganhou ou se houve empate.
>
> Exemplos de execução do programa:
>
>       Digite 0 (pedra), 1 (papel) ou 2 (tesoura)
>       Jogador 1: 0
>       Jogador 2: 1
>       Jogador 2 venceu
>
>       Digite 0 (pedra), 1 (papel) ou 2 (tesoura)
>       Jogador 1: 2
>       Jogador 2: 2
>       Empate
>
>       Digite 0 (pedra), 1 (papel) ou 2 (tesoura)
>       Jogador 1: 2
>       Jogador 2: 1
>       Jogador 1 venceu
>
> ***

> ### **Exercício 2.8 - Dígitos impares em um número de até 3 dígitos**
>
> Faça um programa que recebe do usuário um número de até 3 dígitos e então calcula a quantidade de dígitos ímpares no número.
>
> Exemplos de execução do programa:
>
>       Digite um número inteiro de até 3 dígitos: 204
>       Não há dígitos ímpares em 204.
>
>       Digite um número inteiro de até 3 dígitos: 72
>       Há apenas 1 dígito ímpar em 072.
>
>       Digite um número inteiro de até 3 dígitos: 935
>       Há 3 dígitos ímpares em 935.
>
> ***
