from utils import (
    validar_email,
    validar_telefone,
    validar_nif,
    gerar_id_clientes
)

clientes = []


# CREATE
def criar_cliente(nome, data_nascimento, email, telefone, nacionalidade, morada, nif):

    if not validar_email(email):
        return 500, "Email inválido"

    if not validar_telefone(telefone):
        return 500, "Telefone inválido"

    if not validar_nif(nif):
        return 500, "NIF inválido"

    cliente = {
        "id": gerar_id_clientes(clientes),
        "nome": nome.strip(),
        "data_nascimento": data_nascimento,
        "email": email.strip(),
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