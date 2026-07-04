def formatar(valor):
    return f"{valor:.1f}".replace(".", ",")


def calcular_e_imprimir(sigla, processos):
    total_retorno = 0
    total_resposta = 0
    total_espera = 0
    n = len(processos)

    for p in processos:
        retorno = p.tempo_conclusao - p.chegada
        resposta = p.tempo_primeira_execucao - p.chegada
        espera = retorno - p.duracao

        total_retorno += retorno
        total_resposta += resposta
        total_espera += espera

    media_retorno = total_retorno / n
    media_resposta = total_resposta / n
    media_espera = total_espera / n

    print(f"{sigla} {formatar(media_retorno)} {formatar(media_resposta)} {formatar(media_espera)}")