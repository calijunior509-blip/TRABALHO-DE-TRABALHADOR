# ==============================
# main.py
# ==============================

from passageiros import *
from aeronaves import *
from trabalhadores import *
from bilhetes import *


def mostrar_lugares(id_aeronave, bilhetes, total=30):

    print("\n===== LUGARES =====")

    ocupados = []

    for b in bilhetes:
        if b["id_aeronave"] == id_aeronave:
            ocupados.append(b["lugar"])

    for i in range(1, total + 1):

        if i in ocupados:
            print("[ X ]", end=" ")
        else:
            print(f"[{i:02}]", end=" ")

        if i % 6 == 0:
            print()

    print()


def menu():

    print("\n===== MENU =====")
    print("1 - Criar passageiro")
    print("2 - Listar passageiros")
    print("3 - Buscar passageiro")
    print("4 - Atualizar passageiro")
    print("5 - Remover passageiro")
    print("-------------------")
    print("6 - Criar aeronave")
    print("7 - Listar aeronaves")
    print("8 - Buscar aeronave")
    print("9 - Atualizar aeronave")
    print("10 - Remover aeronave")
    print("-------------------")
    print("11 - Criar trabalhador")
    print("12 - Listar trabalhadores")
    print("13 - Buscar trabalhador")
    print("14 - Atualizar trabalhador")
    print("15 - Remover trabalhador")
    print("-------------------")
    print("16 - Criar bilhete")
    print("17 - Listar bilhetes")
    print("18 - Buscar bilhete")
    print("19 - Remover bilhete")
    print("0 - Sair")


while True:

    menu()

    opcao = input("Opção: ")

    # PASSAGEIROS

    if opcao == "1":

        code, obj = criar_passageiro(
            input("Nome: "),
            input("Data nascimento: "),
            input("Email: "),
            input("Telefone: "),
            input("Nacionalidade: "),
            input("Morada: "),
            input("NIF: ")
        )

        print(obj)

    elif opcao == "2":

        code, obj = listar_passageiros()
        print(obj)

    elif opcao == "3":

        code, obj = buscar_passageiro(
            int(input("ID: "))
        )

        print(obj)

    elif opcao == "4":

        code, obj = atualizar_passageiro(
            int(input("ID: ")),
            input("Novo nome: "),
            input("Novo email: "),
            input("Novo telefone: "),
            input("Nova morada: ")
        )

        print(obj)

    elif opcao == "5":

        code, obj = deletar_passageiro(
            int(input("ID: "))
        )

        print(obj)

    # AERONAVES

    elif opcao == "6":

        code, obj = criar_aeronave(
            input("Nome: "),
            input("Modelo: "),
            input("Lotação: "),
            input("Data construção: "),
            input("Data estreia: "),
            input("Construtora: "),
            input("Tipo: "),
            input("Número motores: ")
        )

        print(obj)

    elif opcao == "7":

        code, obj = listar_aeronaves()
        print(obj)

    elif opcao == "8":

        code, obj = buscar_aeronave(
            int(input("ID: "))
        )

        print(obj)

    elif opcao == "9":

        code, obj = atualizar_aeronave(
            int(input("ID: ")),
            input("Novo nome: "),
            input("Novo modelo: "),
            input("Nova lotação: "),
            input("Novo tipo: ")
        )

        print(obj)

    elif opcao == "10":

        code, obj = deletar_aeronave(
            int(input("ID: "))
        )

        print(obj)

    # TRABALHADORES

    elif opcao == "11":

        code, obj = criar_trabalhador(
            input("Nome: "),
            input("Data nascimento: "),
            input("Nacionalidade: "),
            input("Cargo: "),
            input("Idade: ")
        )

        print(obj)

    elif opcao == "12":

        code, obj = listar_trabalhadores()
        print(obj)

    elif opcao == "13":

        code, obj = buscar_trabalhador(
            int(input("ID: "))
        )

        print(obj)

    elif opcao == "14":

        code, obj = atualizar_trabalhador(
            int(input("ID: ")),
            input("Novo nome: "),
            input("Novo cargo: ")
        )

        print(obj)

    elif opcao == "15":

        code, obj = deletar_trabalhador(
            int(input("ID: "))
        )

        print(obj)

    # BILHETES

    elif opcao == "16":

        id_aeronave = int(input("ID aeronave: "))

        ver = input("Ver lugares? (s/n): ")

        if ver.lower() == "s":

            code, lista = listar_bilhetes()

            if code == 200:
                mostrar_lugares(id_aeronave, lista)

        code, obj = criar_bilhete(
            int(input("ID passageiro: ")),
            id_aeronave,
            input("Origem: "),
            input("Destino: "),
            input("Hora partida: "),
            input("Hora chegada: "),
            input("Lugar: ")
        )

        print(obj)

    elif opcao == "17":

        code, obj = listar_bilhetes()
        print(obj)

    elif opcao == "18":

        code, obj = buscar_bilhete(
            int(input("ID: "))
        )

        print(obj)

    elif opcao == "19":

        code, obj = deletar_bilhete(
            int(input("ID: "))
        )

        print(obj)

    elif opcao == "0":
        break

    else:
        print("Opção inválida")