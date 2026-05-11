from passageiros import buscar_cliente
from aeronaves import buscar_aeronave

bilhetes = []


def gerar_id():
    if not bilhetes:
        return 1
    return bilhetes[-1]["id"] + 1


def lugar_ocupado(id_aeronave, lugar):
    for b in bilhetes:
        if b["id_aeronave"] == id_aeronave and b["lugar"] == lugar:
            return True
    return False


def criar_bilhete(
    id_cliente,
    id_aeronave,
    origem,
    destino,
    hora_partida,
    hora_chegada,
    lugar
):

    # validar cliente
    code, cliente = buscar_cliente(id_cliente)
    if code != 200:
        return 404, "Cliente não encontrado"

    # validar aeronave
    code, aeronave = buscar_aeronave(id_aeronave)
    if code != 200:
        return 404, "Aeronave não encontrada"

    # validar tipo lugar
    try:
        lugar = int(lugar)
    except:
        return 500, "Lugar inválido"

    # validar lugar válido
    if lugar <= 0:
        return 500, "Lugar inválido"

    # validar capacidade
    if lugar > aeronave["lotacao"]:
        return 500, "Lugar excede capacidade do avião"

    # validar ocupado
    if lugar_ocupado(id_aeronave, lugar):
        return 500, "Lugar já ocupado"

    bilhete = {
        "id": gerar_id(),
        "cliente": cliente["nome"],
        "id_cliente": id_cliente,
        "id_aeronave": id_aeronave,
        "origem": origem,
        "destino": destino,
        "hora_partida": hora_partida,
        "hora_chegada": hora_chegada,
        "lugar": lugar
    }

    bilhetes.append(bilhete)

    return 201, bilhete


def listar_bilhetes():
    return 200, bilhetes


def buscar_bilhete(id_bilhete):
    for b in bilhetes:
        if b["id"] == id_bilhete:
            return 200, b

    return 404, "Bilhete não encontrado"


def deletar_bilhete(id_bilhete):
    for b in bilhetes:
        if b["id"] == id_bilhete:
            bilhetes.remove(b)
            return 200, id_bilhete

    return 404, "Bilhete não encontrado"