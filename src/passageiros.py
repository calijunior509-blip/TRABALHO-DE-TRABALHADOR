clientes = []


def gerar_id():
    if not clientes:
        return 1
    return clientes[-1]["id"] + 1


def validar_email(email):
    return "@" in email and "." in email


def validar_telefone(telefone):
    return telefone.isdigit()


def validar_nif(nif):
    return nif.isdigit() and len(nif) == 9


# CREATE
def criar_cliente(nome, data_nascimento, email, telefone, nacionalidade, morada, nif):

    if not validar_email(email):
        return 500, "Email inválido"

    if not validar_telefone(telefone):
        return 500, "Telefone inválido"

    if not validar_nif(nif):
        return 500, "NIF inválido"

    cliente = {
        "id": gerar_id(),
        "nome": nome.strip(),
        "data_nascimento": data_nascimento,
        "email": email.strip(),
        "telefone": telefone,
        "nacionalidade": nacionalidade,
        "morada": morada,
        "nif": nif
    }

    clientes.append(cliente)

    return 201, cliente


# READ
def listar_clientes():
    return 200, clientes


def buscar_cliente(id_cliente):
    for c in clientes:
        if c["id"] == id_cliente:
            return 200, c

    return 404, "Cliente não encontrado."


# UPDATE
def atualizar_cliente(id_cliente, nome=None, email=None, telefone=None, morada=None):
    for c in clientes:
        if c["id"] == id_cliente:

            if nome and nome.strip():
                c["nome"] = nome.strip()

            if email:
                if not validar_email(email):
                    return 500, "Email inválido"
                c["email"] = email.strip()

            if telefone:
                if not validar_telefone(telefone):
                    return 500, "Telefone inválido"
                c["telefone"] = telefone

            if morada and morada.strip():
                c["morada"] = morada.strip()

            return 200, c

    return 404, "Cliente não encontrado."


# DELETE
def deletar_cliente(id_cliente):
    for c in clientes:
        if c["id"] == id_cliente:
            clientes.remove(c)
            return 200, id_cliente

    return 404, "Cliente não encontrado."