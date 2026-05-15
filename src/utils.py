# ==============================
# utils.py
# ==============================

from datetime import datetime


def validar_data(data_texto):
    try:
        data = datetime.strptime(data_texto, "%Y-%m-%d")
        return data <= datetime.now()
    except:
        return False


def validar_cargo(cargo):
    cargos = ["piloto", "copiloto", "assistente de bordo"]
    return cargo.lower().strip() in cargos


def validar_email(email):
    return "@" in email and "." in email


def validar_telefone(telefone):
    return telefone.isdigit()


def validar_nif(nif):
    return nif.isdigit() and len(nif) == 9


def gerar_id(lista):
    if not lista:
        return 1
    return lista[-1]["id"] + 1