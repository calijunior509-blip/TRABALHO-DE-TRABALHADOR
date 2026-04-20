# ==============================
# utils.py
# funções auxiliares
# ==============================


def gerar_id(lista):
    # gera um ID incremental com base na lista existente

    if not lista:
        return 1

    return lista[-1]["id"] + 1