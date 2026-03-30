
from passageiros import (
    criar_cliente, listar_clientes, buscar_cliente,
    atualizar_cliente, deletar_cliente
)

from aeronaves import (
    criar_aeronave, listar_aeronaves, buscar_aeronave,
    atualizar_aeronave, deletar_aeronave
)

def menu_clientes():
    while True:
        print("\n=== MENU CLIENTES ===")
        print("1 - inserir cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Atualizar cliente")
        print("5 - Deletar cliente")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            criar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            atualizar_cliente()
        elif op == "5":
            deletar_cliente()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def menu_aeronaves():
    while True:
        print("\n=== MENU AERONAVES ===")
        print("1 - inserir aeronave")
        print("2 - Listar aeronaves")
        print("3 - Buscar aeronave")
        print("4 - Atualizar aeronave")
        print("5 - Deletar aeronave")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            criar_aeronave()
        elif op == "2":
            listar_aeronaves()
        elif op == "3":
            buscar_aeronave()
        elif op == "4":
            atualizar_aeronave()
        elif op == "5":
            deletar_aeronave()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def menu_principal():
    while True:
        print("\n=== Aeroporto arround the world ===")
        print("1 - Gerir Clientes")
        print("2 - Gerir Aeronaves")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            menu_clientes()
        elif op == "2":
            menu_aeronaves()
        elif op == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida!")


menu_principal()