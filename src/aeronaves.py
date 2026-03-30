aeronaves = []


def gerar_id():
    if not aeronaves:
        return 1
    return aeronaves[-1]["id"] + 1


# CREATE - Cadastrar aeronave
def criar_aeronave():
    print("\n=== Cadastrar Aeronave ===")

    aeronave = {
        "id": gerar_id(),
        "nome": input("Nome: "),
        "modelo": input("Modelo: "),
        "lotacao": int(input("Lotação: ")),
        "data_construcao": input("Data de Construção: "),
        "data_estreia": input("Data de Estreia: "),
        "construtora": input("Construtora: "),
        "tipo": input("Tipo: "),
        "num_motores": int(input("Número de Motores: "))
    }

    aeronaves.append(aeronave)
    print(f"\n✅ Aeronave criada com ID {aeronave['id']}")


# READ - Listar todas
def listar_aeronaves():
    print("\n=== Lista de Aeronaves ===")

    if not aeronaves:
        print("Nenhuma aeronave cadastrada.")
        return

    for a in aeronaves:
        print("\n-------------------")
        print(f"Nome: {a.get('nome', 'N/A')}")
        print(f"tipo: {a.get('tipo', 'N/A')}")


# READ - Buscar por ID
def buscar_aeronave():
    try:
        id_busca = int(input("Digite o ID: "))
        for a in aeronaves:
            if a["id"] == id_busca:
                print("\nAeronave encontrada:")
                for chave, valor in a.items():
                    print(f"{chave.capitalize()}: {valor}")
                return a
        print("❌ Aeronave não encontrada.")
    except ValueError:
        print("ID inválido.")


# UPDATE - Editar aeronave
def atualizar_aeronave():
    print("\n=== Atualizar Aeronave ===")
    aeronave = buscar_aeronave()

    if aeronave:
        print("\nDeixe vazio para manter o valor atual.\n")

        novo_nome = input(f"Nome ({aeronave['nome']}): ")
        if novo_nome:
            aeronave["nome"] = novo_nome

        novo_modelo = input(f"Modelo ({aeronave['modelo']}): ")
        if novo_modelo:
            aeronave["modelo"] = novo_modelo

        nova_lotacao = input(f"Lotação ({aeronave['lotacao']}): ")
        if nova_lotacao:
            aeronave["lotacao"] = int(nova_lotacao)

        novo_tipo = input(f"Tipo ({aeronave['tipo']}): ")
        if novo_tipo:
            aeronave["tipo"] = novo_tipo

        print("✅ Aeronave atualizada com sucesso!")


# DELETE - Remover aeronave
def deletar_aeronave():
    print("\n=== Remover Aeronave ===")
    try:
        id_busca = int(input("Digite o ID: "))
        for a in aeronaves:
            if a["id"] == id_busca:
                aeronaves.remove(a)
                print("🗑️ Aeronave removida com sucesso!")
                return
        print("❌ Aeronave não encontrada.")
    except ValueError:
        print("ID inválido.")
