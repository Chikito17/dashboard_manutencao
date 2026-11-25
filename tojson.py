import csv
import json


# Abrir o CSV
with open("c:\DCV_J.csv", "r", encoding="utf-8") as csv_file: # Colocar o arquivo na pasta c: e referencia-lo
    leitor = csv.DictReader(csv_file)  # Lê o CSV como dicionário
    dados = list(leitor)

# Salvar como JSON
with open("DCV_j.json", "w", encoding="utf-8") as json_file:
    json.dump(dados, json_file, indent=4, ensure_ascii=False)

print("Conversão concluída!")

