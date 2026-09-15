#Exercício 1

# try:
#     valor = int(input("Digite o valor gasto na compra: "))
#     quadrado = valor**2
#     print(f'{quadrado}')
# except ValueError:
#     print('Valor inválido !')

#Exercício 2

# try:
#     valorUm = input("Digite o primeiro valor: ")
#     valorDois = input("Digite o segundo valor: ")
#     if valorUm > valorDois:
#         print(f'O {valorUm} é maior')
#     elif valorUm < valorDois:
#         print(f'O {valorDois} é maior')
#     else:
#        raise ValueError
# except ValueError:
#     print("Os valores inseridos são iguais")

#Exercício 3

# try:
#     letra = str.upper(input("Digite uma letra: "))
#     match letra :
#         case 'A':
#             print("Abacaxi")
#         case 'B':
#             print("Banana")
#         case 'C':
#             print("Carambola")
#         case 'D':
#             print("Damasco")
#         case _ :
#             raise ValueError
# except ValueError:
#     print("Entrada de dado inválida! Por Favor insire uma dessas letras (A,B,C,D)")

#Exercíco 4

# try:
#     salarioMinimo = 1621.00
#     salarioPessoa = float(input("Digite o seu salário: "))
#     qtdeSalarioMin = salarioPessoa/salarioMinimo
#     print(f'Você recebe {qtdeSalarioMin} de salários mínimos')
# except ValueError:
#     print("Valor inválido! Por favor insira um valor válido.")

#Exercício 5

# lista=['a','b','c','d','e','f','g','h']

# def buscar_item_por_indice(lista: list[str], indice: int)-> str:
#     return print(lista[indice])


# try:
#     buscar_item_por_indice(lista , indice=(int(input("Digite um número: "))))
# except ValueError:
#     print('Valor inválido !')
# except IndexError:
#     print("O valor inserido não existe na lista")

#Exercício 6

# preco_produto = {"Banana":1.00, "Maçã": 2.00, "Macarrão":50.00}

# try:
#     nome = str(input("Digite um nome de produto: "))
#     print (f"O valor do {nome} é {preco_produto[nome]}")
# except KeyError:
#     print("O produto inserido não existe na lista")

#Exercício 7

# try:
#     num1 = float(input("Digite o primeiro valor: "))
#     num2 = float(input("Digite o segundo valor: "))
#     media = (num1+num2)/2
#     print(f'A média entre {num1} e {num2} é {media}')
# except ValueError:
#     print("Entrada inválida! ")
# else:
#     print('O cálculo foi realizado com sucesso!')
# finally:
#     print("Código finalizado!")

#Exercício 8

try:
    nome_produto = input("informe o produto desejado: ")

    try:
        quantidade_disp = int(input("Informe a quantidade disponível do produto: "))
        quantidade_comp = int(input("Informe a quantidade desejada do produto: "))
    except ValueError:
        print("Quantidade inválida")
    else:
        if quantidade_comp > quantidade_disp:
            raise ValueError("Estoque insuficiente.")
except TypeError as te:
    print(f'Erro de tipo: {te}')
except ValueError as ve:
    print(f"Valor inválido: {ve}")
else:
    print('Compra realizada')