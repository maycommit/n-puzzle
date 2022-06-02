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

A fila de prioridade utilizada pelo A* neste projeto foi immplementada utilizando a estrutura de dados heap, de modo que a organização do arranjo pode ser visto como uma arvore binaria quase completa.

![heap-order](https://user-images.githubusercontent.com/10244839/171711828-3e9f56a3-3c28-4409-9087-7a7a1c2a4d99.jpg)

A utilização de uma heap para manipulação da fila implicou em um melhor tempo de execução quando comparado a uma implementação utilizando array ordenado.

| Metodo | Tempo (O) |
| --- | ---|
| put | O(log n) |
| get | O(log n) |


[See more...](https://github.com/maycommit/n-puzzle/blob/main/priority_queue.py)

### Nó

[See more...](https://github.com/maycommit/n-puzzle/blob/main/node.py)

### BFS

[See more...](https://github.com/maycommit/n-puzzle/blob/main/bfs.py)

A implementação do algoritmo de busca em largura foi baseada em um exemplo mostrado em sala de aula (Busca: Algoritmo genérico) Aula 03. 
Mais abaixo temos a exemplificação do código feito com algumas observações de pontos importantes para o funcionamento do da solução.    

*  Inicializa a borda com Estado inicial linha 15.  
*  Escolha o nó e remova ele da borda linha 18.   
*  Se encontrar o estado desejado, retorne linha 23. 
*  Adicionar o nó escolhido a expandido linha 28.   
* Expandir o nó escolhido e adicionar os nós resultantes à borda (se este não estiver em borda ou em explorados)  linha 31. 


### A*

[See more...](https://github.com/maycommit/n-puzzle/blob/main/astar.py)

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
- Cui, Xiao & Shi, Hao. (2010). A*-based Pathfinding in Modern Computer Games. 11. 
