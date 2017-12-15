O algoritmo de Dijkstra é extremamente parecido com a abordagem usada por [Prim](https://andrecgro.github.io/Grafos-UFSCAR-2017-2/mst.html), a grande diferença é que o caminho analisado é conservado desde a raiz, e não apenas do nó pai.

Por isso, aconselhamos primeiro o entendimento e estudo do algoritmo de Prim pelo link acima e aqui vamos tentar explicitar apenas as diferenças no código entre os dois algoritmos, tanto para realçar as suas similaridades quanto para não causar redundância nas explicações.

![Figura 1 - Inicializando funções e escolhendo raízes iniciais](https://puu.sh/yHeC4/672d9dbf70.png)  

A primeira grande diferença desta função implementada para o algoritmo de Dijkstra é que ele pode conter vários nós para serem iniciados, ou seja, podemos gerar quantos subgrafos quisermos. A atribuição de nós pais e filhos nesse caso ocorrerá através da concorrência entre as duas raízes escolhida, em nosso caso escolhemos *K* randomicamente na linha 8. Ou seja, quem conquistar um nó como filho primeiro, terá esse nó como seu filho de fato.

![Figura 2 - Checagem de caminhos mínimos para Dijkstra](https://puu.sh/yHeMQ/e1d4299e1c.png)

A segunda, e última, grande diferença entre os dois algoritmos é que a checagem de caminhos mínimos, feita na linha 45 através da atribuição realizada na linha 43, é feita somando o caminho do pai atual até o nó analisado com o caminho da raiz até o pai atual no caso de Dijkstra. Para Prim, isso era feito somente com o caminho do pai atual até o nó analisado na iteração em execução.

Fora isso, podemos tirar como base que são algoritmos extremamente parecidos. Nos casos de testes propostos para o trabalho, executamos este algoritmo com 2 e 3 raízes iniciais, as fotos respectivas podem ser encontradas abaixo.

Para finalizar, gostaríamos de mostrar que a execução do algoritmo elaborado no dataset proposto para *K=2* resultou nos seguintes conjuntos de vértices:
![Figura 3 - Dijkstra com 2 raízes iniciais](https://puu.sh/yHfJs/4d882fe8dd.png)

Já para *K=3* temos os seguintes conjuntos:
![Figura 4 - Dijkstra com 3 raízes iniciais](https://puu.sh/yHfLc/4b5ea0771e.png)