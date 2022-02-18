import json

json_file_path = "C:\\Users\\ivani\\Desktop\\Atalhos\\Colab\\out.json"

eventosList = []
with open(json_file_path) as f:
    eventoDict = json.loads(json.dumps(f.read()))
    eventosList.append(eventoDict)

print("Imprimindo cada Objeto JSON Decodificado")
for evento in eventosList:
    print(eventosList[0])
