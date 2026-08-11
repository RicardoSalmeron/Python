#criar uma função criar_aluno com parametros nome e idades e retorne uma lista


# nome= str(input("Digite o seu nome: "))
#
# idade = int(input("Digite sua idade: "))
#
# def criar_alunos(nome:str, idade:int)->None:
#     lista = [nome, idade]
#     return lista
#
# print(criar_alunos(nome, idade))

#Lista 2

# #exercício 1
# livros = input(str("Digite o nome do produto: "))
# preco = input(float('Digite o preço do produto: '))
# páginas = input(int("Digite a quantidade de páginas do produto: "))

#exercício 2
#def dobrar(numero:int)->int:
    # """ Dobra o número informado ao chamar a função
    # Arg
    #     :numero o número que dever ser duplicado
    #
    # Return:
    #     return: retorna o número informado dobrado
    # """

#     return numero*2
# print(dobrar(100))

#exercício 3
# def calcular_media(notas:list[float])->float:
#     """
#       Calcula uma média de notas
#
#       Args:
#           notas: lista de notas
#
#       Returns:
#           return: retorna a média de notas enviadas à função
#     """

#     return sum(notas) / len(notas)

# print(calcular_media([5,9.8,7,6,2]))

#Exercício 4
# def criar_aluno(nome:str, idade:int, curso:str)-> list(object):
#     """
#         Cria uma lista com o nome e idade e curso de um aluno
#
#         Args:
#             nome: nome do aluno
#             idade: idade do aluno
#             curso: curso do aluno
#
#         Returns:
#             return: lista com o nome, idade e curso do aluno
#     """
#     return [nome, idade, curso]

#Exercício 5
def resumo_carrinho(precos: list(float), desconto:float)->str:
    """"
        Realiza a soma dos produtos em uma lista aplica um desconto e exibe o calor final

        Args:
            precos: uma lista com os preços dos produtos
            desconto: desconto que será aplicado ao produto
            valor_final:realiza a conta para o valor final do produto
        Return:
            retorna o valor final do produto
    """
    valor_final= sum(precos)*(1-(desconto/100))
    return str(f"Total: R${round(valor_final, 2)}")
print(resumo_carrinho([9,80,50,100],30))


def soma_dos_divisores(numero:int)->list(int):
    soma:list = []
    for num in range(1,numero+1):
        if numero % num == 0:
            soma.append(num)
    return soma
print(soma_dos_divisores(6))