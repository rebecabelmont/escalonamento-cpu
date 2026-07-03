#criando a classe processo para armazenar os dados de cada processo
class Processo:
    #construtor da classe para inicializar os atributos do processo
    def __init__(self, id, chegada, duracao):
        self.id = id
        self.chegada = chegada #guarda o momento que ele chegou na fila de processos
        self.duracao = duracao #guarda o tempo que ele precisa para ser executado
         
        self.tempo_restante = duracao
        self.tempo_primeira_execucao = -1 #quando o processo for executado pela primeira vez, esse atributo vai receber o tempo atual do relógio
        self.tempo_conclusao = 0 #guarda o momento que o processo foi concluído