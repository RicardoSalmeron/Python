#Exceções
#são erros que acontecem no tempo de execução de um programa

# valor = float(input("Digite o valor gasto na compra: "))
# qtde = int(input("Digite a quantidade de itens da compra: "))
# ticket_medio = valor/qtde
# print(f"O seu ticket médio é {ticket_medio:.2f}")

# try:
#     valor = float(input("Digite o valor gasto na compra: "))
#     qtde = int(input("Digite a quantidade de itens da compra: "))
#     ticket_medio = valor/qtde
#     print(f"O seu ticket médio é {ticket_medio:.2f}")
# except ZeroDivisionError: 
#     print("Não é possível dividir por 0 (zero) ")
# except ValueError: 
#     print("Valor Inválido! ")



try:
    valor = float(input("Digite o valor gasto na compra: "))
    qtde = int(input("Digite a quantidade de itens da compra: "))
    ticket_medio = valor/qtde
    print(f"O seu ticket médio é {ticket_medio:.2f}")
except ZeroDivisionError: 
    print("Não é possível dividir por 0 (zero) ")
except ValueError: 
    print("Valor Inválido! ")
finally:
    print("Obrigado por comprar no supermercado!")