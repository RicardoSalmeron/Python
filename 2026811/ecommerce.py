nome = 0
preco = 1
estoque = 2

catalogo = []

def cadastrar_produto(catalogo :list[list[object]], nome:str, preco:float, estoque:int):
    """
        Função que realiza o cadastro dos produtos que existe no e-commerce

        Args
            produto: junta as características do produto em um mesma lista
            catalogo: a lista que realizará a junção das listas criadas em produtos

        Return
            catalogo: retorna uma lista compostas das listas criadas no produto
    
    """


    produto = [nome, preco, estoque]
    catalogo.append(produto)
    return catalogo

def exibir_catalogo(catalogo: list[list[object]])->None:
    """
        Função que realiza a separação e exibição dos produtos dentro do catalogo e realiza a exibição

        Args
            catalogo: lista que será separada e exibida

        Return
            return: retorna o catalogo

    """


    for produto in catalogo:
        return f'{produto[nome]} - R$ {produto[preco]:.2f} ({produto[estoque]})'

def get_catalogo():
    return catalogo


# cadastrar_produto(catalogo, "Camiseta Azul", 59.90, 120)
# cadastrar_produto(catalogo, "Tênis Runner", 199.90, 40)
# exibir_catalogo(catalogo)