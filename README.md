Projeto Rota Inteligente: 

1. Otimização para Sabor Express1. Descrição do Problema e Objetivos

A empresa "Sabor Express" enfrenta atrasos em horários de pico e altos custos operacionais devido ao planejamento manual de rotas3. 
O objetivo deste projeto é desenvolver uma solução baseada em Inteligência Artificial para:

- Reduzir o tempo de entrega e o consumo de combustível
- Automatizar a definição de trajetos utilizando a teoria de grafos.
- Agrupar pedidos próximos para otimizar o trabalho dos entregadores

  
2. Abordagem Adotada

A solução foi construída em duas camadas lógicas fundamentais:
- Nível Estratégico (Clustering): Divisão dos pedidos em zonas geográficas para evitar que entregadores percorram distâncias desnecessárias entre uma entrega e outra.
- Nível Operacional (Busca em Grafos): Cálculo da rota exata dentro de cada zona, tratando ruas como arestas e esquinas como nós de um grafo.


3. Algoritmos Utilizados
   
- K-Means: Algoritmo de aprendizado não supervisionado que realiza o agrupamento de entregas baseando-se na proximidade espacial (latitude e longitude)
- Algoritmo $A^*$ (A-estrela): Utilizado para encontrar o menor caminho. Ele supera algoritmos como BFS e DFS por utilizar uma heurística, o que torna a busca mais eficiente em mapas urbanos complexos.


4. Diagrama do Modelo

O modelo representa a região central como um grafo ponderado11.

- Nós: Pontos de entrega e interseções de ruas12.
- Arestas: Ruas com pesos definidos por distância ou tempo estimado de tráfego.


5. Análise de Resultados e Eficiência
   
- Eficiência: A solução reduz drasticamente o erro humano e o tempo de planejamento. Inspirada no sistema ORION da UPS, a aplicação de heurísticas permite economias significativas em escala 
rea.
- Limitações: O modelo atual utiliza pesos estáticos. Em cenários reais, a inclusão de dados de tráfego via IoT seria necessária para maior precisão15.
- Melhorias: Sugere-se a implementação de Aprendizado por Reforço (RL) para ajustes dinâmicos 
conforme o entregador se desloca.
