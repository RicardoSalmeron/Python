import requests

#Exercício 0
# try:
#     cep = input('Digite o cep: ')
#     response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
#     if response.status_code == 200:
#         dicionario = response.json()
#         if 'erro' in dicionario:
#             print('CEP inexistente')
#         else:
#             print(f"Rua: {dicionario['logradouro']}")
#             print(f"Bairro: {dicionario['bairro']}")
#     else:
#         print(f'Erro de requisição: {response.status_code}')
# except requests.exceptions.ConnectionError as erro:
#         print('Erro. Erro de Conexão com API')
# except Exception as erro:
#         print(f'Erro: {erro}')

#Exercício 1
# try:
#     uf = input('Digite a sigla de uma UF: ')
#     response = requests.get(f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')
   
#     if response.status_code == 200:
#         estado = response.json()
#         for municipio in estado:
#             print(f'{municipio.get('id')}: {municipio.get('nome')}')    
# except requests.exceptions.ConnectionError:
#     print('Erro de conexão.')

#Exercício 2
# try:
#     n=input("Digite a quantidade de nomes desejados: ")
#     response= requests.get(f'http://randomuser.me/api/?results={n}')
#     if response.status_code == 200:
#         listaNomes = response.json()
#         nomes = listaNomes.get('results')
#         for i in nomes:
#             ordem = [i.get('name').get('first')]
#             print(sorted(ordem))
        
# except requests.exceptions.ConnectionError:
#     print('Erro de conexão.')

#Exercício 3
# try:
#     ingredient = input("Digite o ingrediente desejado na receita (EM INGLÊS): ")
#     response = requests.get(f'http://dummyjson.com/recipes?limit=50')
#     if response.status_code == 200:
#         recipes = response.json().get('recipes')
#         for i in recipes:
#             if ingredient in i.get('ingredients'):
#                 print(i.get('name'))
# except requests.exceptions.ConnectionError:
#     print('Erro de conexão.')

#Exercício 4
# try:
#     response = requests.get(f'http://dummyjson.com/products?limit=100')
#     if response.status_code == 200:
#         produtos = response.json().get('products')
#         valor= 0
#         for produto in produtos:
#             valor += ((float(produto.get('price')) - (float(produto.get('price'))*float(produto.get('discountPercentage'))/100))* float(produto.get('stock')))
#         print(valor)
        
# except requests.exceptions.ConnectionError:
#     print('Erro de conexão.')

#Exercício 5

try:
    moedas = input("Digite as moedas que gostaria de comparar: ")
    response = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moedas}')
    resposta = moedas.replace('-',"")
    compra = resposta.get('bid')
    venda = resposta.get('ask')
    print(compra, venda)
except requests.exceptions.ConnectionError:
    print('Erro de conexão.')

