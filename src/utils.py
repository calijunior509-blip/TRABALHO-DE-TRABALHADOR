from datetime import datetime


def validar_data(data_texto):
    try:
        if not isinstance(data_texto, str):
            return False

        data = datetime.strptime(data_texto, "%Y-%m-%d")

        if data > datetime.now():
            return False

        return True

    except ValueError:
        return False


def validar_cargo(cargo):
    cargos_validos = ["piloto", "copiloto", "assistente de bordo"]
    return cargo.lower().strip() in cargos_validos


def validar_email(email):
    return "@" in email and "." in email


def validar_telefone(telefone):
    return telefone.isdigit()


def validar_nif(nif):
    return nif.isdigit() and len(nif) == 9


def gerar_id_trabalhadores(lista):
    if not lista:
        return 1

    return lista[-1]["id"] + 1


def gerar_id_clientes(lista):
    if not lista:
        return 1

    return lista[-1]["id"] + 1