# README — viagem.pay ✈️

## Descrição

O **viagem.pay** é um sistema de gestão de viagens aéreas feito em Python no terminal.

O projeto permite:

* Gestão de passageiros
* Gestão de aeronaves
* Gestão de trabalhadores
* Gestão de bilhetes
* Reserva de lugares
* Validação de dados
* Visualização de lugares ocupados

Tudo funciona através de um menu interativo no terminal.

---

# Estrutura do Projeto

```bash
viagem.pay/
│
├── main.py
├── passageiros.py
├── aeronaves.py
├── trabalhadores.py
├── bilhetes.py
├── utils.py
└── README.md
```

---

# Funcionalidades

## Passageiros

* Criar passageiro
* Listar passageiros
* Buscar passageiro
* Atualizar passageiro
* Remover passageiro

---

## Aeronaves

* Criar aeronave
* Listar aeronaves
* Buscar aeronave
* Atualizar aeronave
* Remover aeronave

---

## Trabalhadores

* Criar trabalhador
* Listar trabalhadores
* Buscar trabalhador
* Atualizar trabalhador
* Remover trabalhador

### Cargos válidos

* piloto
* copiloto
* assistente de bordo

---

## Bilhetes

* Criar bilhete
* Listar bilhetes
* Buscar bilhete
* Remover bilhete

### Validações

O sistema valida:

* Existência do passageiro
* Existência da aeronave
* Lugares repetidos
* Capacidade da aeronave
* Lugares inválidos

---

# Sistema de Lugares

Ao criar um bilhete é possível visualizar os lugares disponíveis da aeronave.

Exemplo:

```bash
[01] [02] [03] [ X ] [05] [06]
[07] [08] [09] [10] [ X ] [12]

X = ocupado
```

---

# Validações Implementadas

## Datas

Formato obrigatório:

```bash
YYYY-MM-DD
```

---

## Email

Verifica:

```bash
@
.
```

---

## Telefone

Aceita apenas números.

---

## NIF

O NIF deve possuir:

* 9 dígitos
* Apenas números

---

# Tecnologias Utilizadas

* Python 3
* Estruturas de dados com listas e dicionários
* Programação modular

---

# Objetivo do Projeto

Este projeto foi desenvolvido com objetivo educativo para praticar:

* CRUD em Python
* Modularização
* Validações
* Organização de código
* Manipulação de listas e dicionários
* Menus interativos

---

# Melhorias Futuras

* Persistência com ficheiros JSON
* Integração com base de dados
* Interface gráfica
* Login de administrador
* Sistema de voos
* Datas e horários reais
* API REST

---

# Autor

Carlos Silva(e chatGPT)
