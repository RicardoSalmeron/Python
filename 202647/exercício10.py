salario=float(input("Indique o valor do salário"))
vendas=float(input("Indique o valor das vendas"))
if vendas>1500:
    comissao= vendas*0.03
else:
    comissao= vendas*0.05
total= salario+comissao
print(f'{total}')