from metricas import calcular_e_imprimir


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
    pass


def escalonador_rr(processos):
    pass