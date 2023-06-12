# Desafio Eletrônica 1 - Semana 1

- Como posso reduzir a tensão de saida de uma bateria utilizando apenas resistores?
  - [Slide 17][slideOriginal]
  - Onde:
    - V = 12V
    - V desejada = 3V

## Solução

- Tendo em vista que a tensão de um gerador, como a bateria neste exemplo, é diretamente afetada pela pela resistência e pela corrente seguindo a lei de Ohm:
  ```
  V = R.i
  ```
- Existem várias maneiras de se resolver esse mesmo problema. Uma delas seria a de colocar um resistor interno na bateria para que a tensão de saida dela fosse menor do que a tensão real, seguindo a seguinte formula, derivada da lei acima:
  ```
  V= ε-R.i
  ```
- Onde ε seria a tensão real, e V seria a tensão oferecida ao restante do circuito. Nesse caso, como somente a resistência importa, é possivel supor um valor qualquer para a corrente:
  ```
  V = 3V
  ε = 12V
  R = ?
  i = 1A
  ```
- Resolvendo a equação:
  ```
  3 = 12-R.1
  -9 = -R
  R = 9Ω
  ```
- Abrindo a bateria, o circuito final teria essa cara, considerando que além dela, o circuito em si pode ser qualquer um:

  [Imagem do Caderno, se deu erro me fale][linkImagem]

[slideOriginal]: https://onedrive.live.com/view.aspx?resid=424F790CAA1D8958!1510&ithint=file%2cpptx&authkey=!ABis8Cf20bgfNdo
[linkImagem]: https://drive.google.com/file/d/1mrvelusgvIjKMJ5FKT7sJe5DYsGtN0ME/view?usp=sharing
