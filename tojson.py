import csv
import json


# Abrir o CSV
with open("c:\DCV700_F.csv", "r", encoding="utf-8") as csv_file: # Colocar o arquivo na pasta c: e referencia-lo
   leitor = csv.DictReader(csv_file)  # Lê o CSV como dicionário
   dados = list(leitor)

# Salvar como JSON
with open("DCV700_F.json", "w", encoding="utf-8") as json_file:
    json.dump(dados, json_file, indent=4, ensure_ascii=False)

print("Conversão concluída!")

