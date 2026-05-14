# ==============================
# database.py
# ==============================

import json
import os


def carregar(nome_ficheiro):

    if not os.path.exists(nome_ficheiro):
        return []

    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def guardar(nome_ficheiro, dados):

    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)