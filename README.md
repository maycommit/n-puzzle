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

No metodo de resoluçao de problemas utlizado é necessario a criação de uma arvore de estados para que o algoritmo de busca encontre o melhor caminho. Cada nó da arvore de estados contem informções importantes para o funcionamento do algorimo, como id, ação, estado e custo real. Além disso ele dispõe de metodos que auxiliam em sua manipulação como a geração de nós filhos utilizando seu proprio estado e manipulação de matrizes.

Quando expandido o nó pode retornar até quatro filhos dependendo de seu estado atual. A cada expansão seu custo real é incrementado, assim como sua profundidade. Os estados gerados dependem das regras de movimentação ja detalhadas acima.

![Screen Shot 2022-06-02 at 17 47 43](https://user-images.githubusercontent.com/10244839/171735352-f43f5879-eb29-4863-8e42-0784ac00285a.png)

[See more...](https://github.com/maycommit/n-puzzle/blob/main/node.py)

### BFS

Para um melhor entendimento sobre o algoritmo A* foi implementado a busca em largura baseado no algoritmo busca_em_arvore. Como uma busca nao informada, ela não faz o uso de heuristicas e sua implementação é baseada em fila FIFO. Também conhecida como força bruta.

[See more...](https://github.com/maycommit/n-puzzle/blob/main/bfs.py)

### Heuristicas

  #### Distância de Manhattan
 - A distância de Manhattan é um modelo geométrico em que a distância entre dois pontos é a soma das diferenças absolutas em suas coordenadas. Esta função retorna o somatório do cálculo de manhattan para cada ponto da matriz.

 #### Número de Peças Fora do Lugar
  - Utilizando o método de comparar a posição do elemento corrente na matriz em relação a sua  posição no estado final conseguimos obter o somatório de quantas posições estão erradas. 

#### Distancia de Manhattan

### A*

O algoritmo foi baseado na busca em largura mencionada acima, porem sua implementação é baseado em uma fila de prioridade e nas heuristicas requisitadas. Além disso para cada nó expandido é calculado um custo utilizando `f(x) = g(x) + h(x)`. Estes custos definem as operação que serao realizadas na fila de prioridade.

[See more...](https://github.com/maycommit/n-puzzle/blob/main/astar.py)

### Viewer
Para visualizar os resultados das execuções basta visualizar em seu navegador acessando `http://localhost:8000` após executar o comando:
```
python --m http.server --directory ./out 8000
```

As execuções sao salvas em diretorios cujo nome é composto por estado inicial concatenado com o estado final. Ao entrar no diretorio uma pagina semelhante ao exemplo deve ser exibida:

![Screen Shot 2022-06-02 at 11 14 14](https://user-images.githubusercontent.com/10244839/171650203-33adff6a-d2db-4eab-9bb8-c50a6e213fa2.png)
<img width="1258" alt="Screen Shot 2022-06-02 at 16 24 46" src="https://user-images.githubusercontent.com/10244839/171721560-906617f9-e492-4d6a-b755-371aba02d060.png">


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
