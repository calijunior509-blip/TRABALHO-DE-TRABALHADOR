# ==============================
# aeronaves.py
# ==============================

from utils import gerar_id
from basididadus import carregar, guardar

aeronaves = carregar("aeronaves.json")


def criar_aeronave(
    nome,
    modelo,
    lotacao,
    data_construcao,
    data_estreia,
    construtora,
    tipo,
    num_motores
):

    try:
        lotacao = int(lotacao)
        num_motores = int(num_motores)
    except:
        return 500, "Valores inválidos"

    if lotacao <= 0 or num_motores <= 0:
        return 500, "Valores inválidos"

    aeronave = {
        "id": gerar_id(aeronaves),
        "nome": nome,
        "modelo": modelo,
        "lotacao": lotacao,
        "data_construcao": data_construcao,
        "data_estreia": data_estreia,
        "construtora": construtora,
        "tipo": tipo,
        "num_motores": num_motores
    }

    aeronaves.append(aeronave)

    guardar("aeronaves.json", aeronaves)

    return 201, aeronave


def listar_aeronaves():
    return 200, aeronaves


def buscar_aeronave(id_aeronave):
    for a in aeronaves:
        if a["id"] == id_aeronave:
            return 200, a

    return 404, "Aeronave não encontrada"


def atualizar_aeronave(
    id_aeronave,
    nome=None,
    modelo=None,
    lotacao=None,
    tipo=None
):

    for a in aeronaves:
        if a["id"] == id_aeronave:

            if nome:
                a["nome"] = nome

            if modelo:
                a["modelo"] = modelo

            if lotacao:
                try:
                    lotacao = int(lotacao)

                    if lotacao <= 0:
                        return 500, "Lotação inválida"

                    a["lotacao"] = lotacao

                except:
                    return 500, "Lotação inválida"

            if tipo:
                a["tipo"] = tipo

            guardar("aeronaves.json", aeronaves)

            return 200, a

    return 404, "Aeronave não encontrada"


def deletar_aeronave(id_aeronave):
    for a in aeronaves:
        if a["id"] == id_aeronave:

            aeronaves.remove(a)

            guardar("aeronaves.json", aeronaves)

            return 200, "Aeronave removida"

    return 404, "Aeronave não encontrada"