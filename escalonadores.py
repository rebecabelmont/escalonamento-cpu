from collections import deque
from metricas import calcular_e_imprimir
from processo import Processo


def escalonador_fcfs(processos):
    fila = sorted(processos, key=lambda p: p.chegada)
    tempo_atual = 0
    for p in fila:
        if tempo_atual < p.chegada:
            tempo_atual = p.chegada
        p.tempo_primeira_execucao = tempo_atual
        tempo_atual += p.duracao
        p.tempo_conclusao = tempo_atual
    calcular_e_imprimir("FCFS", processos)


def escalonador_sjf(processos):
    processos = [Processo(p.id, p.chegada, p.duracao) for p in processos]
    nao_iniciados = processos[:]
    nao_iniciados.sort(key=lambda p: p.chegada)

    tempo_atual = 0
    processos_concluidos = 0
    n = len(processos)
    while processos_concluidos < n:
        prontos = [p for p in nao_iniciados if p.chegada <= tempo_atual]

        if not prontos:
            tempo_atual = nao_iniciados[0].chegada
            continue

        prontos.sort(key=lambda p: (p.duracao, p.chegada))
        escolhido = prontos[0]
        escolhido.tempo_primeira_execucao = tempo_atual
        tempo_atual += escolhido.duracao
        escolhido.tempo_conclusao = tempo_atual
        nao_iniciados.remove(escolhido)
        processos_concluidos += 1
    calcular_e_imprimir("SJF", processos)


def escalonador_rr(processos):
    processos = [Processo(p.id, p.chegada, p.duracao) for p in processos]
    quantum = 2
    chegadas = sorted(processos, key=lambda p: p.chegada)

    fila = deque()
    tempo_atual = 0
    proximo = 0
    concluidos = 0
    n = len(processos)

    while concluidos < n:
        while proximo < n and chegadas[proximo].chegada <= tempo_atual:
            fila.append(chegadas[proximo])
            proximo += 1

        if not fila:
            tempo_atual = chegadas[proximo].chegada
            continue

        atual = fila.popleft()
        if atual.tempo_primeira_execucao == -1:
            atual.tempo_primeira_execucao = tempo_atual

        executado = min(quantum, atual.tempo_restante)
        tempo_atual += executado
        atual.tempo_restante -= executado

        while proximo < n and chegadas[proximo].chegada <= tempo_atual:
            fila.append(chegadas[proximo])
            proximo += 1

        if atual.tempo_restante == 0:
            atual.tempo_conclusao = tempo_atual
            concluidos += 1
        else:
            fila.append(atual)

    calcular_e_imprimir("RR", processos)