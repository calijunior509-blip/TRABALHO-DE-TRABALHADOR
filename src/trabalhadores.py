from utils import validar_data, validar_cargo, gerar_id_trabalhadores

trabalhadores = []


def criar_trabalhador(nome, data_nascimento, nacionalidade, cargo, idade):
    if not validar_data(data_nascimento):
        return 500, "Data inválida (YYYY-MM-DD)"

    if not validar_cargo(cargo):
        return 500, "Cargo inválido"

    try:
        idade = int(idade)
        if idade <= 0 or idade > 120:
            return 500, "Idade inválida"
    except:
        return 500, "Idade inválida"

    trabalhador = {
        "id": gerar_id_trabalhadores(trabalhadores),
        "nome": nome.strip(),
        "data_nascimento": data_nascimento,
        "nacionalidade": nacionalidade,
        "cargo": cargo.strip().lower(),
        "idade": idade
    }

    trabalhadores.append(trabalhador)

    return 201, trabalhador


def listar_trabalhadores():
    if not trabalhadores:
        return 404, "Nenhum trabalhador registado"

    return 200, trabalhadores


def buscar_trabalhador(id_trabalhador):
    for t in trabalhadores:
        if t["id"] == id_trabalhador:
            return 200, t

    return 404, "Trabalhador não encontrado"


def atualizar_trabalhador(id_trabalhador, nome=None, cargo=None):
    for t in trabalhadores:
        if t["id"] == id_trabalhador:

            if nome and nome.strip():
                t["nome"] = nome.strip()

            if cargo:
                if not validar_cargo(cargo):
                    return 500, "Cargo inválido"
                t["cargo"] = cargo.strip().lower()

            return 200, t

    return 404, "Trabalhador não encontrado"


def deletar_trabalhador(id_trabalhador):
    for t in trabalhadores:
        if t["id"] == id_trabalhador:
            trabalhadores.remove(t)
            return 200, id_trabalhador

    return 404, "Trabalhador não encontrado"