# Projeto 01 - Escalonamento de CPU

Implementação de algoritmos de escalonamento de processos para a disciplina de Sistemas Operacionais. 

## Algoritmos Implementados
O simulador executa uma lista de processos e gera estatísticas para os seguintes algoritmos:
- **FCFS** (First-Come, First-Served)
- **SJF** (Shortest Job First)
- **RR** (Round Robin) com quantum = 2

## Métricas Avaliadas
Para cada algoritmo, o programa emite os valores médios para:
1. Tempo de retorno
2. Tempo de resposta
3. Tempo de espera

## Formato de Entrada e Saída
- **Entrada:** Um arquivo de texto lido até o EOF, contendo pares de números inteiros separados por espaço (tempo de chegada e duração do processo).
- **Saída:** Impressão no terminal de três linhas contendo a sigla do algoritmo e os valores das três métricas na ordem exata solicitada.
