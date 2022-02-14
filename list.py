import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

dados = dados[0]

dados = dados.decode("utf-8")

print(dados['descricao'],encoding='utf-8')