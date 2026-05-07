# ==============================
# main.py (viagem.pay 😄)
# sistema completo
# ==============================

from passageiros import (
    criar_cliente, listar_clientes, buscar_cliente,
    atualizar_cliente, deletar_cliente
)

from aeronaves import (
    criar_aeronave, listar_aeronaves, buscar_aeronave,
    atualizar_aeronave, deletar_aeronave
)

from trabalhadores import (
    criar_trabalhador, listar_trabalhadores, buscar_trabalhador,
    atualizar_trabalhador, deletar_trabalhador
)

from bilhetes import (
    criar_bilhete, listar_bilhetes, buscar_bilhete, deletar_bilhete
)


# ==============================
# ASCII LUGARES (CORRIGIDO)
# ==============================

def mostrar_lugares(id_aeronave, bilhetes, total=30):
    print("\n===== MAPA DE LUGARES =====")

    ocupados = []

    for b in bilhetes:
        try:
            if b["id_aeronave"] == id_aeronave:
                ocupados.append(b["lugar"])
        except:
            pass

    for i in range(1, total + 1):
        if i in ocupados:
            print("[ X ]", end=" ")
        else:
            print(f"[{i:02}]", end=" ")

        if i % 6 == 0:
            print()

    print("\nX = ocupado | número = livre\n")


def menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Consultar cliente")
    print("4 - Atualizar cliente")
    print("5 - Remover cliente")
    print("--------------------------")
    print("6 - Criar aeronave")
    print("7 - Listar aeronaves")
    print("8 - Consultar aeronave")
    print("9 - Atualizar aeronave")
    print("10 - Remover aeronave")
    print("--------------------------")
    print("11 - Criar trabalhador")
    print("12 - Listar trabalhadores")
    print("13 - Consultar trabalhador")
    print("14 - Atualizar trabalhador")
    print("15 - Remover trabalhador")
    print("--------------------------")
    print("16 - Criar bilhete")
    print("17 - Listar bilhetes")
    print("18 - Consultar bilhete")
    print("19 - Remover bilhete")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        # ======================
        # CLIENTES
        # ======================

        if opcao == "1":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            nacionalidade = input("Nacionalidade: ")
            morada = input("Morada: ")
            nif = input("NIF: ")

            code, obj = criar_cliente(
                nome,
                data_nascimento,
                email,
                telefone,
                nacionalidade,
                morada,
                nif
            )

            print(obj if code == 201 else f"Erro: {obj}")

        elif opcao == "2":
            code, obj = listar_clientes()
            print(obj if code == 200 else f"Erro: {obj}")

        elif opcao == "3":
            try:
                id_c = int(input("ID do cliente: "))
                code, obj = buscar_cliente(id_c)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        elif opcao == "4":
            try:
                id_c = int(input("ID do cliente: "))
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")
                morada = input("Nova morada: ")

                code, obj = atualizar_cliente(
                    id_c,
                    nome if nome else None,
                    email if email else None,
                    telefone if telefone else None,
                    morada if morada else None
                )

                print(obj if code == 200 else f"Erro: {obj}")

            except:
                print("Erro na atualização.")

        elif opcao == "5":
            try:
                id_c = int(input("ID do cliente: "))
                code, obj = deletar_cliente(id_c)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        # ======================
        # AERONAVES
        # ======================

        elif opcao == "6":
            nome = input("Nome: ")
            modelo = input("Modelo: ")
            lotacao = input("Lotação: ")
            data_construcao = input("Data de Construção: ")
            data_estreia = input("Data de Estreia: ")
            construtora = input("Construtora: ")
            tipo = input("Tipo: ")
            num_motores = input("Número de Motores: ")

            code, obj = criar_aeronave(
                nome,
                modelo,
                int(lotacao),
                data_construcao,
                data_estreia,
                construtora,
                tipo,
                int(num_motores)
            )

            print(obj if code == 201 else f"Erro: {obj}")

        elif opcao == "7":
            code, obj = listar_aeronaves()
            print(obj if code == 200 else f"Erro: {obj}")

        elif opcao == "8":
            try:
                id_a = int(input("ID da aeronave: "))
                code, obj = buscar_aeronave(id_a)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        elif opcao == "9":
            try:
                id_a = int(input("ID da aeronave: "))

                nome = input("Novo nome: ")
                modelo = input("Novo modelo: ")
                lotacao = input("Nova lotação: ")
                tipo = input("Novo tipo: ")

                code, obj = atualizar_aeronave(
                    id_a,
                    nome if nome else None,
                    modelo if modelo else None,
                    int(lotacao) if lotacao else None,
                    tipo if tipo else None
                )

                print(obj if code == 200 else f"Erro: {obj}")

            except:
                print("Erro na atualização.")

        elif opcao == "10":
            try:
                id_a = int(input("ID da aeronave: "))
                code, obj = deletar_aeronave(id_a)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        # ======================
        # TRABALHADORES
        # ======================

        elif opcao == "11":
            nome = input("Nome: ")
            data_nascimento = input("Data nascimento (YYYY-MM-DD): ")
            nacionalidade = input("Nacionalidade: ")
            cargo = input("Cargo (piloto/copiloto/assistente de bordo): ")
            idade = input("Idade: ")

            code, obj = criar_trabalhador(
                nome,
                data_nascimento,
                nacionalidade,
                cargo,
                idade
            )

            print(obj if code == 201 else f"Erro: {obj}")

        elif opcao == "12":
            code, obj = listar_trabalhadores()
            print(obj if code == 200 else f"Erro: {obj}")

        elif opcao == "13":
            try:
                id_t = int(input("ID do trabalhador: "))
                code, obj = buscar_trabalhador(id_t)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        elif opcao == "14":
            try:
                id_t = int(input("ID do trabalhador: "))
                nome = input("Novo nome: ")
                cargo = input("Novo cargo: ")

                code, obj = atualizar_trabalhador(
                    id_t,
                    nome if nome else None,
                    cargo if cargo else None
                )

                print(obj if code == 200 else f"Erro: {obj}")

            except:
                print("Erro na atualização.")

        elif opcao == "15":
            try:
                id_t = int(input("ID do trabalhador: "))
                code, obj = deletar_trabalhador(id_t)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        # ======================
        # BILHETES
        # ======================

        elif opcao == "16":
            try:
                id_cliente = int(input("ID do cliente: "))
                id_aeronave = int(input("ID da aeronave: "))

                ver = input("Ver lugares? (s/n): ")
                if ver.lower() == "s":
                    code, lista_bilhetes = listar_bilhetes()
                    if code == 200:
                        mostrar_lugares(id_aeronave, lista_bilhetes)

                origem = input("Origem: ")
                destino = input("Destino: ")
                hora_partida = input("Hora de partida: ")
                hora_chegada = input("Hora de chegada: ")
                lugar = int(input("Lugar: "))

                code, obj = criar_bilhete(
                    id_cliente,
                    id_aeronave,
                    origem,
                    destino,
                    hora_partida,
                    hora_chegada,
                    lugar
                )

                print(obj if code == 201 else f"Erro: {obj}")

            except:
                print("Erro ao criar bilhete.")

        elif opcao == "17":
            code, obj = listar_bilhetes()
            print(obj if code == 200 else f"Erro: {obj}")

        elif opcao == "18":
            try:
                id_b = int(input("ID do bilhete: "))
                code, obj = buscar_bilhete(id_b)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        elif opcao == "19":
            try:
                id_b = int(input("ID do bilhete: "))
                code, obj = deletar_bilhete(id_b)
                print(obj if code == 200 else f"Erro: {obj}")
            except:
                print("ID inválido.")

        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()