# ==============================
# trabalhadores.py
# ==============================

from utils import validar_data, validar_cargo, gerar_id
from basididadus import carregar, guardar

trabalhadores = carregar("trabalhadores.json")


def criar_trabalhador(
    nome,
    data_nascimento,
    nacionalidade,
    cargo,
    idade
):

    if not validar_data(data_nascimento):
        return 500, "Data inválida"

    if not validar_cargo(cargo):
        return 500, "Cargo inválido"

    try:
        idade = int(idade)

        if idade <= 0 or idade > 120:
            return 500, "Idade inválida"

    except:
        return 500, "Idade inválida"

    trabalhador = {
        "id": gerar_id(trabalhadores),
        "nome": nome,
        "data_nascimento": data_nascimento,
        "nacionalidade": nacionalidade,
        "cargo": cargo.lower(),
        "idade": idade
    }

    trabalhadores.append(trabalhador)

    guardar("trabalhadores.json", trabalhadores)

    return 201, trabalhador


def listar_trabalhadores():
    trabalhadores = carregar("trabalhadores.json")
    return 200, trabalhadores


def buscar_trabalhador(id_trabalhador):
    trabalhadores = carregar("trabalhadores.json")
    for t in trabalhadores:
        if t["id"] == id_trabalhador:
            return 200, t

    return 404, "Trabalhador não encontrado"


def atualizar_trabalhador(id_trabalhador, nome=None, cargo=None):
    trabalhadores = carregar("trabalhadores.json")

    for t in trabalhadores:
        if t["id"] == id_trabalhador:

            if nome:
                t["nome"] = nome

            if cargo:

                if not validar_cargo(cargo):
                    return 500, "Cargo inválido"

                t["cargo"] = cargo.lower()

            guardar("trabalhadores.json", trabalhadores)

            return 200, t

    return 404, "Trabalhador não encontrado"


def deletar_trabalhador(id_trabalhador):
    trabalhadores = carregar("trabalhadores.json")
    for t in trabalhadores:
        if t["id"] == id_trabalhador:

            trabalhadores.remove(t)

            guardar("trabalhadores.json", trabalhadores)

            return 200, "Trabalhador removido"

    return 404, "Trabalhador não encontrado"