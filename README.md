# n-puzzle
Este repositório contém a implementação de alguns algoritmos clássicos em IA como objetivo de resolver o game n-puzzle.

## Sobre

### Movimentação
No jogo em questão o usuário tem a possibilidade de realizar até quatro movimentos. Essa movimentação depende da posição do espaço vazio pelo tabuleiro, onde:
- Espaço vazio ao centro possibilita 4 movimentos.
- Espaço vazio nos cantos possibilita 3 movimentos.
- Espaço vazio nas bordas possibilita 2 movimentos.


![8-Puzzle](https://user-images.githubusercontent.com/10244839/171637818-2696c415-b0fd-4858-b27f-2b27d4397b62.jpg)
![8-Puzzle-1](https://user-images.githubusercontent.com/10244839/171637855-11cf0ecb-202a-4e4d-80ab-e743a927bc14.jpg)
![8-Puzzle-2](https://user-images.githubusercontent.com/10244839/171637858-1f3407be-3598-49f4-99cc-9f7ec9aaba1a.jpg)

Seguindo o padrão acima as possibilidade de movimentos são geradas por `get_all_possible_movements(n)` onde n é a coordenada do espaço vazio no tabuleiro.
As possibilidades são calculdas incrementando a linha e coluna apartir das coordenadas do espaço vazio onde `0 <= possibilidade < PUZZLE_SIZE`.
- UP: (x + 1, y) 
- DOWN: (x - 1, y)
- RIGHT: (x, y - 1)
- LEFT: (x, y + 1)

[See more...](https://github.com/maycommit/n-puzzle/blob/main/movement.py)

### Fila de prioridades

### Nó

### BFS

### A*

### Viewer
Para visualizar os resultados das execuções basta visualizar em seu navegador acessando `http://localhost:8000` após executar o comando:
```
python --m http.server --directory ./out 8000
```

As execuções sao salvas em diretorios cujo nome é composto por estado inicial concatenado com o estado final. Ao entrar no diretorio uma pagina semelhante ao exemplo deve ser exibida:

![Screen Shot 2022-06-02 at 11 14 14](https://user-images.githubusercontent.com/10244839/171650203-33adff6a-d2db-4eab-9bb8-c50a6e213fa2.png)


## Desenvolvimento

### Pré requisitos
- Python 3.8+

### Run
Para rodar o projeto basta executar o arquivo principal mudando a entrada padrão com o comando:
```
python main.py < input.txt
```

### Tests
Para executar os testes unitarios execute o comando abaixo: 
```
python -m unittest discover -s ./ -p '*_test.py'
```

## Referencias
- Cormen, T. H., Leiserson, C. E., Rivest, R. L.,, Stein, C. (2001). Introduction to Algorithms. The MIT Press. ISBN: 0262032937
- Russell, S., Norvig, P. (2010). Artificial Intelligence: A Modern Approach. Prentice Hall.
- Ramalho, L. (2015). Fluent Python. ISBN: 9781491946008 1491946008
