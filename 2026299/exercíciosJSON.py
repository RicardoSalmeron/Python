#Exercício 1
import json
# arqNotas = open("notas.txt", 'r', encoding="utf-8")
# dicNotas = {}

# for linha in arqNotas.readlines():
#     textoLinha = linha.strip()
#     rm = textoLinha.strip().split(',')[0]
#     nome = textoLinha.strip().split(',')[1]
#     notas = textoLinha.strip().split(',')[2:len(textoLinha.split(','))]
#     dicNotas[rm]= {"nome": nome, "notas": notas}

# with open("notas.json", 'w', encoding='utf-8') as arqNotas1:
#     json.dump(dicNotas, arqNotas1, indent=2, ensure_ascii=False)

# #Exercício 2 
# arqFood = open("foods.txt", 'r', encoding="utf-8")
# dicFood = {}
# for linha in arqFood.readlines():
#     textoLinha = linha.strip()
#     id = textoLinha.strip().split(',')[1]     
#     nome = textoLinha.strip().split(',')[0]
#     food = textoLinha.strip().split(',')[2]
#     dicFood[id]= {"nome": nome, "food": food}
# with open("food.json", 'w', encoding='utf-8') as arqFood1:
#     json.dump(dicFood, arqFood1, indent=2, ensure_ascii=False)


#Exercício 3
nomes = []
with open("heroes.json", 'r', encoding="utf-8") as arqHerois:
    herois = json.load(arqHerois)
    members = herois.get("members")
    for membro in members:
        powers = membro.get('powers')
        for poder in powers:
            if poder == "Flight":
                nomes.append(membro.get("name"))
print(nomes)