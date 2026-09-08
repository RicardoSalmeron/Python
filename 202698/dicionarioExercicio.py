#Exercício 1

# pessoas = {}
# for i in range(5):
#     cpf:int= input("Digite o seu CPF: ")
#     if len(cpf) != 11:
#         print(ValueError("Tamanho de CPF inválido!"))
#     nome:str = input("Digite o seu nome: ")
#     pessoas[cpf] = nome

# print (pessoas)

#Exercício 2 
produtos = {}
for i in range(5):
    produto = input("Produto: ")
    valor = float(input(f'Valor de {produto}: '))
    produtos[produto] = valor

for produto, valor in produto.items():
    if valor>50:
        print(f'{produto}: {valor}')

#Exercício 3
alunosNotas = {}
for i in range(3):
    rm = int(input("Digite o seu rm: "))
    n1 = int(input("Digite a sua primeira nota: "))
    n2 = int(input("Digite a sua segunda nota: "))
    n3 = int(input("Digite a sua terceira nota: "))
    notas = [n1, n2, n3]
    alunosNotas[rm] = notas
print(alunosNotas)