aeronaves = []


def gerar_id():
    if not aeronaves:
        return 1
    return aeronaves[-1]["id"] + 1


# CREATE
def criar_aeronave(nome, modelo, lotacao, data_construcao, data_estreia, construtora, tipo, num_motores):

    try:
        lotacao = int(lotacao)
        num_motores = int(num_motores)
    except:
        return 500, "Dados numéricos inválidos"

    if lotacao <= 0 or num_motores <= 0:
        return 500, "Valores inválidos"

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


# READ
def listar_aeronaves():
    return 200, aeronaves


def buscar_aeronave(id_aeronave):
    for a in aeronaves:
        if a["id"] == id_aeronave:
            return 200, a

    return 404, "Aeronave não encontrada."


# UPDATE
def atualizar_aeronave(id_aeronave, nome=None, modelo=None, lotacao=None, tipo=None):
    for a in aeronaves:
        if a["id"] == id_aeronave:

            if nome and nome.strip():
                a["nome"] = nome

            if modelo and modelo.strip():
                a["modelo"] = modelo

            if lotacao:
                try:
                    lotacao = int(lotacao)
                    if lotacao > 0:
                        a["lotacao"] = lotacao
                except:
                    return 500, "Lotação inválida"

            if tipo and tipo.strip():
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