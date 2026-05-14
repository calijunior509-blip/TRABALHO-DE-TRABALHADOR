# ==============================
# passageiros.py
# ==============================

from utils import (
    validar_data,
    validar_email,
    validar_telefone,
    validar_nif,
    gerar_id
)

from basididadus import carregar, guardar

passageiros = carregar("passageiros.json")


def criar_passageiro(
    nome,
    data_nascimento,
    email,
    telefone,
    nacionalidade,
    morada,
    nif
):

    if not validar_data(data_nascimento):
        return 500, "Data inválida"

    if not validar_email(email):
        return 500, "Email inválido"

    if not validar_telefone(telefone):
        return 500, "Telefone inválido"

    if not validar_nif(nif):
        return 500, "NIF inválido"

    passageiro = {
        "id": gerar_id(passageiros),
        "nome": nome,
        "data_nascimento": data_nascimento,
        "email": email,
        "telefone": telefone,
        "nacionalidade": nacionalidade,
        "morada": morada,
        "nif": nif
    }

    passageiros.append(passageiro)

    guardar("passageiros.json", passageiros)

    return 201, passageiro


def listar_passageiros():
    return 200, passageiros


def buscar_passageiro(id_passageiro):
    for p in passageiros:
        if p["id"] == id_passageiro:
            return 200, p

    return 404, "Passageiro não encontrado"


def atualizar_passageiro(
    id_passageiro,
    nome=None,
    email=None,
    telefone=None,
    morada=None
):

    for p in passageiros:
        if p["id"] == id_passageiro:

            if nome:
                p["nome"] = nome

            if email:
                if not validar_email(email):
                    return 500, "Email inválido"
                p["email"] = email

            if telefone:
                if not validar_telefone(telefone):
                    return 500, "Telefone inválido"
                p["telefone"] = telefone

            if morada:
                p["morada"] = morada

            guardar("passageiros.json", passageiros)

            return 200, p

    return 404, "Passageiro não encontrado"


def deletar_passageiro(id_passageiro):
    for p in passageiros:
        if p["id"] == id_passageiro:
            passageiros.remove(p)

            guardar("passageiros.json", passageiros)

            return 200, "Passageiro removido"

    return 404, "Passageiro não encontrado"