#Exercício 1 
def mostrar_informações(nome: str, idade: int, cidade: str):
    return(f'Olá {nome}, você tem {idade} anos e mora em {cidade}')

print(mostrar_informações("Teste", 15, "Roberto"))

#Exercíio 2
def calcular_area_retangulo(base: float =1, altura: float =1):
    area= base*altura
    return area

#Exercício 3
def soma(a:float,b:float):
    return a+b

#Exercício 4
def enviar_email(destinatario,corpo ="", assunto = "Sem assunto" ):
    return (f"E-mail enviado para {destinatario}, com o assunto {assunto}, e com a seguinte mensagem {corpo}")

#Exercício 5
def concatenar_strings(str1:str, str2:str, separador= " "):
    return str1 + separador + str2

#Exercício 6
def comprar_produto(produto = "Produto desconhecido", quantidade: int = 1):
    return(f'Você comprou {quantidade} de {produto}')

#Exercício 7
def test(itens:list[str]):
    for i in itens: 
        print (f'{i}')