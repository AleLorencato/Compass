import json
with open("person.json") as arquivo:
    data = json.load(arquivo)

print(data)
