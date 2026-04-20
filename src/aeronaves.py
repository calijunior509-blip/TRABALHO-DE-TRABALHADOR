# ==============================
# aeronave.py
# CRUD simples para entidade Aeronave
# SEM utilização de classes
# armazenamento em lista
# validações feitas aqui (não no main)
# ==============================

aeronaves = []


# gerar id incremental
def gerar_id():
    # gera um ID incremental com base na lista existente

    if not aeronaves:
        return 1

    return aeronaves[-1]["id"] + 1


# CREATE
def criar_aeronave(nome, modelo, lotacao, data_construcao, data_estreia, construtora, tipo, num_motores):
    aeronave = {
        "id": gerar_id(),
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

    return 201, aeronave


# READ (listar todas)
def listar_aeronaves():
    if not aeronaves:
        return 404, "Nenhuma aeronave cadastrada."

    return 200, aeronaves


# READ (consultar por ID)
def buscar_aeronave(id_aeronave):
    for a in aeronaves:
        if a["id"] == id_aeronave:
            return 200, a

    return 404, "Aeronave não encontrada."


# UPDATE
def atualizar_aeronave(id_aeronave, nome=None, modelo=None, lotacao=None, tipo=None):
    for a in aeronaves:
        if a["id"] == id_aeronave:

            if nome:
                a["nome"] = nome

            if modelo:
                a["modelo"] = modelo

            if lotacao:
                a["lotacao"] = lotacao

            if tipo:
                a["tipo"] = tipo

            return 200, a

    return 404, "Aeronave não encontrada."


# DELETE
def deletar_aeronave(id_aeronave):
    for a in aeronaves:
        if a["id"] == id_aeronave:
            aeronaves.remove(a)
            return 200, id_aeronave

    return 404, "Aeronave não encontrada."