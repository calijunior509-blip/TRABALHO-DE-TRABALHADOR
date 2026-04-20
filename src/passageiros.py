# ==============================
# cliente.py
# CRUD simples para entidade Cliente
# SEM utilização de classes
# armazenamento em lista
# validações feitas aqui (não no main)
# ==============================

clientes = []


# gerar id incremental
def gerar_id():
    # gera um ID incremental com base na lista existente

    if not clientes:
        return 1

    return clientes[-1]["id"] + 1


# CREATE
def criar_cliente(nome, data_nascimento, email, telefone, nacionalidade, morada, nif):
    cliente = {
        "id": gerar_id(),
        "nome": nome,
        "data_nascimento": data_nascimento,
        "email": email,
        "telefone": telefone,
        "nacionalidade": nacionalidade,
        "morada": morada,
        "nif": nif
    }

    clientes.append(cliente)

    return 201, cliente


# READ (listar todos)
def listar_clientes():
    if not clientes:
        return 404, "Nenhum cliente cadastrado."

    return 200, clientes


# READ (consultar por ID)
def buscar_cliente(id_cliente):
    for c in clientes:
        if c["id"] == id_cliente:
            return 200, c

    return 404, "Cliente não encontrado."


# UPDATE
def atualizar_cliente(id_cliente, nome=None, email=None, telefone=None, morada=None):
    for c in clientes:
        if c["id"] == id_cliente:

            if nome:
                c["nome"] = nome

            if email:
                c["email"] = email

            if telefone:
                c["telefone"] = telefone

            if morada:
                c["morada"] = morada

            return 200, c

    return 404, "Cliente não encontrado."


# DELETE
def deletar_cliente(id_cliente):
    for c in clientes:
        if c["id"] == id_cliente:
            clientes.remove(c)
            return 200, id_cliente

    return 404, "Cliente não encontrado."