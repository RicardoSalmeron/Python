#Ricardo Salmerón Paulino de Souza
#RM:572916
#Exercício 1 azulejos
bn1= float(input("Indique o comprimento do banheiro: "))
bn2= float(input("Indique o largura do banheiro: "))
bn3= float(input("Indique o altura do banheiro: "))
an1= float(input("Indique a largura do azulejo em centimetros: "))
an2= float(input("Indique a altura do azulejo em centimetros: "))
calcp1 = (bn1*bn3)*2
calcp2 = (bn2*bn3)*2
calca = (an1*an2)/100
azl1 = calcp1/calca
azl2 = calcp2/calca
caixas = (alz1+alz2)/10
print(f"São necessárias {caixas} caixas de azulejos")