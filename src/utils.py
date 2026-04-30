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


def gerar_id(lista):
    if not lista:
        return 1

    return lista[-1]["id"] + 1