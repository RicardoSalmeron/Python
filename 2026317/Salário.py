n1 = input("Informe o seu nome: ")
n2 = int(input("Informe a quantidade de carros vendidos: "))
n3 = float(input("Informe o valor total de suas vendas: "))
comissao = (n2*200)
venda = (n3/50)
salario = 2500+comissao+venda
print("Seu salário,", n1, "é de", salario)