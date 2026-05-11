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

    return clientes[-1]["id"] + 1

# CREATE - Criar cliente
def criar_cliente():
    print("\n=== Cadastrar Cliente ===")

# CREATE
def criar_cliente(nome, data_nascimento, email, telefone, nacionalidade, morada, nif):
    cliente = {
        "id": gerar_id(),
        "nome": input("Nome: "),
        "data_nascimento": input("Data de Nascimento (dd/mm/aaaa): "),
        "email": input("Email: "),
        "telefone": input("Telefone: "),
        "nacionalidade": input("Nacionalidade: "),
        "morada": input("Morada: "),
        "nif": input("NIF: ")
        "nome": nome,
        "data_nascimento": data_nascimento,
        "email": email,
        "telefone": telefone,
        "nacionalidade": nacionalidade,
        "morada": morada,
        "nif": nif
    }

    clientes.append(cliente)
    print(f"\n✅ Cliente criado com ID {cliente['id']}")

    return 201, cliente

# READ - Listar todos
def listar_clientes():
    print("\n=== Lista de Clientes ===")

# READ (listar todos)
def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
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
        print("\n-------------------")
        print(f"Nome: {c.get('nome', 'N/A')}")
        print(f"Data_nascimento: {c.get('data_nascimento', 'N/A')}")


# READ - Buscar por ID
def buscar_cliente():
    try:
        id_busca = int(input("Digite o ID: "))
        for c in clientes:
            if c["id"] == id_busca:
                print("\nCliente encontrado:")
                for chave, valor in c.items():
                    print(f"{chave.capitalize()}: {valor}")
                return c
        print("❌ Cliente não encontrado.")
    except ValueError:
        print("ID inválido.")


# UPDATE - Atualizar cliente
def atualizar_cliente():
    print("\n=== Atualizar Cliente ===")
    cliente = buscar_cliente()

    if cliente:
        print("\nDeixe vazio para manter o valor atual.\n")

        novo_nome = input(f"Nome ({cliente['nome']}): ")
        if novo_nome:
            cliente["nome"] = novo_nome

        novo_email = input(f"Email ({cliente['email']}): ")
        if novo_email:
            cliente["email"] = novo_email

        novo_telefone = input(f"Telefone ({cliente['telefone']}): ")
        if novo_telefone:
            cliente["telefone"] = novo_telefone

        nova_morada = input(f"Morada ({cliente['morada']}): ")
        if nova_morada:
            cliente["morada"] = nova_morada

        print("✅ Cliente atualizado com sucesso!")


# DELETE - Remover cliente
def deletar_cliente():
    print("\n=== Remover Cliente ===")
    try:
        id_busca = int(input("Digite o ID: "))
        for c in clientes:
            if c["id"] == id_busca:
                clientes.remove(c)
                print("🗑️ Cliente removido com sucesso!")
                return
        print("❌ Cliente não encontrado.")
    except ValueError:
        print("ID inválido.")
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