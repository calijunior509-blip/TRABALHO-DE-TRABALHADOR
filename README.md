# Sistema de Gestão de Aeroporto ✈️

Sistema desenvolvido em Python para gestão de:

- Passageiros
- Aeronaves
- Trabalhadores
- Bilhetes

O projeto funciona em terminal/console e possui persistência de dados em arquivos JSON.

---

# Funcionalidades

## Passageiros

- Criar passageiro
- Listar passageiros
- Buscar passageiro
- Atualizar passageiro
- Remover passageiro

---

## Aeronaves

- Criar aeronave
- Listar aeronaves
- Buscar aeronave
- Atualizar aeronave
- Remover aeronave

---

## Trabalhadores

- Criar trabalhador
- Listar trabalhadores
- Buscar trabalhador
- Atualizar trabalhador
- Remover trabalhador

---

## Bilhetes

- Criar bilhete
- Listar bilhetes
- Buscar bilhete
- Remover bilhete
- Ver lugares ocupados da aeronave

---

# Persistência de Dados

O sistema utiliza arquivos `.json` para guardar os dados automaticamente.

Arquivos criados:

- `passageiros.json`
- `aeronaves.json`
- `trabalhadores.json`
- `bilhetes.json`

Os dados permanecem guardados mesmo após fechar o programa.

---

# Estrutura do Projeto

```bash
projeto/
│
├── main.py
├── passageiros.py
├── aeronaves.py
├── trabalhadores.py
├── bilhetes.py
├── utils.py
├── database.py
│
├── passageiros.json
├── aeronaves.json
├── trabalhadores.json
└── bilhetes.json
