import ecommerce


def menu_cadastrar_produto():
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço unitário do produto: "))
    estoque = int(input("Digite a quantidade exitstente do produto: "))

    ecommerce.cadastrar_produto(ecommerce.get_catalogo(), nome, preco, estoque)


menu_cadastrar_produto()
print(ecommerce.exibir_catalogo(ecommerce.get_catalogo()))
