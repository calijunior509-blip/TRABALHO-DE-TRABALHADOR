# ==============================
# bilhetes.py
# ==============================

from passageiros import buscar_passageiro
from aeronaves import buscar_aeronave
from utils import gerar_id
from basididadus import carregar, guardar

bilhetes = carregar("bilhetes.json")


def lugar_ocupado(id_aeronave, lugar):

    for b in bilhetes:
        if b["id_aeronave"] == id_aeronave and b["lugar"] == lugar:
            return True

    return False


def criar_bilhete(
    id_passageiro,
    id_aeronave,
    origem,
    destino,
    hora_partida,
    hora_chegada,
    lugar
):

    code, passageiro = buscar_passageiro(id_passageiro)

    if code != 200:
        return 404, "Passageiro não encontrado"

    code, aeronave = buscar_aeronave(id_aeronave)

    if code != 200:
        return 404, "Aeronave não encontrada"

    try:
        lugar = int(lugar)
    except:
        return 500, "Lugar inválido"

    if lugar <= 0:
        return 500, "Lugar inválido"

    if lugar > aeronave["lotacao"]:
        return 500, "Lugar excede capacidade"

    if lugar_ocupado(id_aeronave, lugar):
        return 500, "Lugar ocupado"

    bilhete = {
        "id": gerar_id(bilhetes),
        "passageiro": passageiro["nome"],
        "id_passageiro": id_passageiro,
        "id_aeronave": id_aeronave,
        "origem": origem,
        "destino": destino,
        "hora_partida": hora_partida,
        "hora_chegada": hora_chegada,
        "lugar": lugar
    }

    bilhetes.append(bilhete)

    guardar("bilhetes.json", bilhetes)

    return 201, bilhete


def listar_bilhetes():
    bilhetes = carregar("bilhetes.json")
    return 200, bilhetes


def buscar_bilhete(id_bilhete):
    bilhetes = carregar("bilhetes.json")

    for b in bilhetes:
        if b["id"] == id_bilhete:
            return 200, b

    return 404, "Bilhete não encontrado"


def deletar_bilhete(id_bilhete):
    bilhetes = carregar("bilhetes.json")

    for b in bilhetes:
        if b["id"] == id_bilhete:

            bilhetes.remove(b)

            guardar("bilhetes.json", bilhetes)

            return 200, "Bilhete removido"

    return 404, "Bilhete não encontrado"