import json

json_file_path = "C:\\Users\\ivani\\Desktop\\Atalhos\\Colab\\out.json"
#  Substituir as únicas por duplas

with open(json_file_path) as f:

   invalid_json = f.read()

# Substitui todas ' por "
valid_json = invalid_json.replace("None", '"None"')

# Salva o texto modificano no arquivo
with open(json_file_path, "w") as f:
    f.write(valid_json)