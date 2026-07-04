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
    processos = [Processo(p.id, p.chegada, p.duracao) for p in processos]  #cria uma cópia dos processos
    nao_iniciados = processos[:] #cria uma cópia da lista de processos para manipulação
    nao_iniciados.sort(key=lambda p: p.chegada) #ordena os processos pela chegada
    
    tempo_atual = 0
    processos_concluidos = 0
    n = len(processos)

    while processos_concluidos < n:
        #filtra os processos que já chegaram e ainda não foram concluídos
        prontos = [p for p in nao_iniciados if p.chegada <= tempo_atual]
        
        if not prontos:
            tempo_atual = nao_iniciados[0].chegada  #avança o tempo para o próximo processo que vai chegar
            continue
        
        prontos.sort(key=lambda p: (p.duracao, p.chegada))  #ordena os processos prontos pelo tempo de duração e chegada
        escolhido = prontos[0]  #pega o processo com menor duração  
        escolhido.tempo_primeira_execucao = tempo_atual #marca o tempo atual como o momento da primeira execução do processo
        tempo_atual += escolhido.duracao #atualiza o tempo atual somando a duração do processo
        escolhido.tempo_conclusao = tempo_atual #marca o tempo atual como o momento da conclusão do processo

        nao_iniciados.remove(escolhido)  #remove o processo da lista de não iniciados
        processos_concluidos += 1

    calcular_e_imprimir("SJF", processos)     


def escalonador_rr(processos):
    pass