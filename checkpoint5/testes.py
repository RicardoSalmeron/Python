# animais = ('cachorro', 'gato', 'papagaio', 'cachorro')
# print(animais[-1])

# try:
#     diarias = int(input("Quantidade de diárias:"))
#     print(f'Total de diárias reservadas: {diarias}')
# except ValueError:
#     print("Entrada Inválida")

# frase = "Python para Analise de Dados"
# palavras = frase.split()
# sigla = ''
# for palavra in palavras:
#     sigla += palavra[0].upper()
# print(sigla[::-1])


# entregas = (
#     ("em transito", 120.00),
#     ("entregue", 85.50),
#     ("atrasado", 200.00),
#     ("entregue", 60.00),
#     ("atrasado", 150.00),
#     ("em transito", 90.00),
    
# )
# total_atrasado = 0
# qtde_atrasado = 0
# for status, valor in entregas:
#     if status == "atrasado":
#         total_atrasado += valor
#         qtde_atrasado += 1
# print(total_atrasado / qtde_atrasado)

# pacote = ("lisboa", 10, 3200.00, 'cafe da manha', 'passeio de barco', "city tour")
# destino,dias,preco, *incluidos = pacote
# print(incluidos, len(incluidos))

# prescricoes =[("Paciente A", "Dipirona"), ("Paciente B", "Paracetamol"),
#               ("Paciente C", "Dipirona"), ("Paciente D", "Ibuprofeno"),
#               ("Paciente E", "Dipirona"), ("Paciente F", "Paracetamol")]

# contagem ={}
# for paciente, remedio in prescricoes:
#     contagem[remedio] = contagem.get(remedio, 0 )+1

# mais_usado = max(contagem, key=contagem.get)
# print(mais_usado, contagem[mais_usado])

# acervo = {'sala 1': {'quadro': 5, 'escultura':2}, 'sala 2': {'quadro': 3} }
# copia = acervo.copy()
# copia['sala 1']['quadro']=99
# copia['sala 3'] = {'quadro':1}
# print(acervo)

# entradas = ['2', 'dez', '-3', '4']
# total_ingressos = 0
# erros = 0
# for entrada in entradas:
#     try:
#         qtde = int(entrada)
#         if qtde <0:
#             raise ValueError("quantidade negativa")
#         total_ingressos += qtde
#     except ValueError:
#         erros += 1

# print(total_ingressos,erros)

# def validar_pedido(estoque, pedido, preco_unit):
#     if pedido <=0:
#         raise ValueError("Quantidade deve ser positiva")
#     if pedido > estoque:
#         raise ValueError(f'Estoque insuficiente, disponível: {estoque}')
#     return pedido * preco_unit

# pedidos = [(10, 3, 25.0), (5, 8, 40.0), (7, -2, 15.0)]
# total_vendido = 0
# falhas = 0

# for estoque, pedido, preco in pedidos:
#     try:
#         total_vendido += validar_pedido(estoque, pedido, preco)
#     except ValueError:
#         falhas +=1

# print(total_vendido, falhas)

# soma_normais = 0
# qtd_normais = 0
# with open('resultados.txt','r', encoding='utf-8') as arq:
#     for linha in arq:
#         nome, valor, status = linha.strip().split(',')
#         if status == 'Normal':
#             soma_normais += int(valor)
#             qtd_normais += 1
# print(soma_normais / qtd_normais)

# convidados =[("Ana", True),("Bruno", False),("Carla", True),("Diego", True),("Eva", False)]
# with open("confirmados.txt", 'w', encoding='utf-8') as arq:
#     for nome, confirmado in convidados:
#         if confirmado:
#             arq.write(f'{nome}\n')

# with open("confirmados.txt", 'r', encoding='utf-8') as arq:
#     linhas_lidas = arq.readlines()

# print(linhas_lidas)
# print(len(linhas_lidas))

# medidas = (23.5,18.2,30.1,15.8,27.4,19.9,22.0)
# pares_indice = tuple(v for i, v in enumerate(medidas) if i % 2 ==0)
# print(pares_indice[1:-1])

# titulos = ['Código Aberto', "Mundo Digital", "Fuga Silenciosa"]
# resultado =[]
# for titulo in titulos:
#     iniciais = ''.join(palavra[0] for palavra in titulo.split())
#     resultado.append(iniciais.lower()[::-1])
# print(resultado)

# tabela = (
#     ("Leões", 8, 12),
#     ("Tigres", 6, 9),
#     ("Águias", 8, 15),
#     ('Falvões', 6, 15),
# )

# aproveitamento = {}
# for nome, jogos, pontos in tabela:
#     aproveitamento[nome] = round(pontos / (jogos * 3) * 100, 1)

# melhor = max(aproveitamento, key=aproveitamento.get)
# print(melhor, aproveitamento[melhor])

# pedidos = ['pizza', 'sushi', 'temaki', 'pizza', 'churrasco', 'sushi', 'pizza']
# cardapio_precos = {'pizza':45.0, 'sushi':60.0, 'churrasco': 80.0}

# total = 0
# nao_encontrados = []

# for pedido in pedidos:
#     try:
#         total += cardapio_precos[pedido]
#     except KeyError:
#         nao_encontrados.append(pedido)
# print(total, nao_encontrados)

# total_consumo = 0
# registros_validos = 0
# registros_invalidos = 0

# with open('consumo.txt', 'r', encoding='utf-8') as arq:
#     for linha in arq:
#         campos = linha.strip().split(',')
#         try:
#             consumo = float(campos[1])
#             total_consumo += consumo
#             registros_validos += 1
#         except (ValueError, IndexError):
#             registros_validos +=1

# print(total_consumo, registros_validos, registros_invalidos)

voos = []
with open('voos.txt', 'r', encoding='utf-8') as arq:
    for linha in arq:
        campos = linha.strip().split(',')
        atrasos = [int(x) for x in campos[2:]]
        media = sum(atrasos)/ len(atrasos)
        voos.append((campos[0],media))
voos_ordenados = sorted(voos, key=lambda v: v[1], reverse=True)
print(voos_ordenados[0])