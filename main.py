import sys
from processo import Processo
from escalonadores import escalonador_fcfs, escalonador_sjf, escalonador_rr

def ler_processos():
    #lendo a entrada até o EOF e retornando uma lista de processos
    processos = []
    id_atual = 1

    #sys.stdin lê o que o terminal jogar para o programa
    for linha in sys.stdin:
        if not linha.strip():  #ignora linhas em branco
            continue

        partes = linha.strip().split() #divide a linha em partes separadas por espaço
        if len(partes) == 2: #se a linha tiver 2 partes, é um processo com chegada e duração
            #guarda o momento que ele chegou na fila e o tempo que ele precisa para ser executado
            chegada = int(partes[0])
            duracao = int(partes[1])
            processos.append(Processo(id_atual, chegada, duracao)) #adiciona a lista
            id_atual += 1
        
    return processos

if __name__ == "__main__":
    lista_processos = ler_processos() #lendo a entrada e armazenando na lista de processos

    if lista_processos:
        #executa os três escalonadores e imprime os resultados
        escalonador_fcfs(lista_processos)
        escalonador_sjf(lista_processos)
        escalonador_rr(lista_processos)