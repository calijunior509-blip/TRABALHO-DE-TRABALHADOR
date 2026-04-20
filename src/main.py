# ==============================
# main.py
# menu terminal unificado estilo utilizador
# ==============================

from passageiros import (
    criar_cliente, listar_clientes, buscar_cliente,
    atualizar_cliente, deletar_cliente
)

from aeronaves import (
    criar_aeronave, listar_aeronaves, buscar_aeronave,
    atualizar_aeronave, deletar_aeronave
)


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
            email = input("Email: ")

            code, obj = criar_cliente(nome, email)
            if code == 201:
                print("Cliente criado com sucesso:", obj)
            else:
                print("Erro:", obj)

        elif opcao == "2":
            code, obj = listar_clientes()
            if code == 200:
                print("Lista de clientes:")
                for id_c, dados in obj.items():
                    print(f"ID: {id_c} | Nome: {dados['nome']} | Email: {dados['email']}")
            else:
                print("Erro:", obj)

        elif opcao == "3":
            id_c = input("ID do cliente: ")
            code, obj = buscar_cliente(id_c)

            if code == 200:
                print(f"Cliente {id_c}:")
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "4":
            id_c = input("ID do cliente: ")

            nome = input("Novo nome (enter para manter): ")
            email = input("Novo email (enter para manter): ")

            code, obj = atualizar_cliente(
                id_c,
                nome if nome else None,
                email if email else None
            )

            if code == 200:
                print("Cliente atualizado:", obj)
            else:
                print("Erro:", obj)

        elif opcao == "5":
            id_c = input("ID do cliente: ")
            code, obj = deletar_cliente(id_c)

            if code == 200:
                print("Cliente removido:", obj)
            else:
                print("Erro:", obj)

        # ======================
        # AERONAVES
        # ======================

        elif opcao == "6":
            modelo = input("Modelo: ")
            capacidade = input("Capacidade: ")

            code, obj = criar_aeronave(modelo, capacidade)
            if code == 201:
                print("Aeronave criada:", obj)
            else:
                print("Erro:", obj)

        elif opcao == "7":
            code, obj = listar_aeronaves()
            if code == 200:
                print("Lista de aeronaves:")
                for id_a, dados in obj.items():
                    print(f"ID: {id_a} | Modelo: {dados['modelo']} | Capacidade: {dados['capacidade']}")
            else:
                print("Erro:", obj)

        elif opcao == "8":
            id_a = input("ID da aeronave: ")
            code, obj = buscar_aeronave(id_a)

            if code == 200:
                print(f"Aeronave {id_a}:")
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "9":
            id_a = input("ID da aeronave: ")

            modelo = input("Novo modelo (enter para manter): ")
            capacidade = input("Nova capacidade (enter para manter): ")

            code, obj = atualizar_aeronave(
                id_a,
                modelo if modelo else None,
                capacidade if capacidade else None
            )

            if code == 200:
                print("Aeronave atualizada:", obj)
            else:
                print("Erro:", obj)

        elif opcao == "10":
            id_a = input("ID da aeronave: ")
            code, obj = deletar_aeronave(id_a)

            if code == 200:
                print("Aeronave removida:", obj)
            else:
                print("Erro:", obj)

        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()