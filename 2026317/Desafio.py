n1 = float(input("Indique a temperatura em Farenheint: "))
n2= 5
calculo = (n1-32)/1.8
vermelho = '\033[1;31m'
ciano = '\033[1;34m'
print(f'A temperatura é, {vermelho}{n2}, {ciano}{round(calculo,2)}')