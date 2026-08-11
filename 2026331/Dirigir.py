titulo = "Dirigir"
print(f'{titulo:^30}')
idade =int(input("Que idade você tem?: "))
cnh = input("Você tem CNH? ")
#operadores RELACIONAIS
#São os que vão combinar as comparações
#AND é o operador MALVADO, só deixa prosseguir se tudo for SIM
#OR é o opreador BONZINHO, qualquer um que for SIM deixa prosseguir
#NOT é do CONTRA, ele faz tudo ao contrário

if idade >=18 and cnh == 'sim':
    print("Você pode dirigir")
else:
    print("Não pode dirigir")
print("TRANSITO DE SÃO PAULO AGRADECE")