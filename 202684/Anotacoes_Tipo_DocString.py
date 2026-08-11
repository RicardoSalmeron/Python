#Python tem tipagem dinamica

x=10
print(type(x))
nome = "Paulo"
print(type(nome))

#type Hints ajuda a definir o tipo de dados esperados na variável
#mas é apenas uma AJUDA, ou seja não o python não impede que seja atríbuido
#um valor com outro tipo de dado

nome: str = 'Paulo'
print(type(nome))

nome = 123
print(type(nome))

preco: float
preco = 7.8
print(type(preco))

#todos os tipos de dados são aceitos no type hints
#int, float, bool, str, list, etc
disponivel: bool = True
print(type(disponivel))

#o tipo de uso mais importante é quando definimos funções
#Qunado definimos o tipo de dado esperado como parâmetro e tbm o tipo
#de retorono da função, estamos definindo a ASSINATURA da função
#isso é importante para disponibilizarmos essas funções, por exemplo,
#como API

def calcular_total(preco:float, quantidade:int)->float:
    return preco * quantidade

print(calcular_total(preco, 2))
print(calcular_total(preco, 3))

#e quando a função não tem retorno?
def exibir_produto(produto:str, preco:float)->None:
    print(f'{produto} - {preco}')

exibir_produto("leite",9.8)

#revisao de list
#--> tipo de dados composto
minhaLista:list = ['café', 'chantilly', 'biscoito']
print(minhaLista)

dadosPessoais = ['Ricardo', 18, 'masculino', 'superior']
print(dadosPessoais)
print(f'Nome: {dadosPessoais[0]}')
print(f'Idade: {dadosPessoais[1]}')
dadosPessoais.append("Professor")
print(dadosPessoais)
print("Imprimindo a lista elemento a elemento")
for item in dadosPessoais:
    print(item)

#mas e o tipo list?
#vamos aplicar a lista usando type hint em funcoes

def somar_precos(precos:list)->float:
    total: float = 0
    #fale que o total é um float sem falar que é um float
    # total =0.0
    for preco in precos:
        total += preco
    return total
print('\nSomando precos')
print(f'total: {somar_precos([10, 20, 30])}')
#print(preco)
def criar_produto(produto:str, preco:float, quantidade:int)->list:
    return [produto, preco, quantidade]
print(f"\nCriar Estoque")
print(f'Estoque:{criar_produto('Leite', 8.9, 10)}')

#tipo de dados generico: object
#quando usar -> na assinatura da função
#entendimento
idades: list[int] =[17, 54, 23]
print(f'Idades: {idades}')

#se quisessse uma lista mista
produto = ["camisa", 29.8, 8]
print(f'Produto: {produto}')
produto: list[object] = ["camisa", 28.9, 8]


#Docstring
#documenta a função
def calcular_total(preco:float, quantidade:int)->float:
    """"Calcula a quantidade total de um produto

    Args:
        :param preço: preço unitário do produto
        :param quantidade: quantidade total de um produto

    Returns:
        total: preço total (preço * quantidade)

    """
    total: float = preco * quantidade
    return total