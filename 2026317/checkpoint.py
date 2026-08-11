#Ricardo Salmerón Paulino de Souza
#RM:572916
#Exercício 1 azulejos
#bn1= float(input("Indique o comprimento do banheiro: "))
#bn2= float(input("Indique o largura do banheiro: "))
#bn3= float(input("Indique o altura do banheiro: "))
#an1= float(input("Indique a largura do azulejo em centimetros: "))
#an2= float(input("Indique a altura do azulejo em centimetros: "))
#calcp1 = (bn1*bn3)*2
#calcp2 = (bn2*bn3)*2
#calca = (an1/100)*(an2/100)
#azl1 = calcp1/calca
#azl2 = calcp2/calca
#caixas = (azl1+azl2)/10
#print(f"São necessárias {round(caixas,2)} caixas de azulejos")

#Exercício Compra com Subtotal
arrz= 22.9
fei= 7.50
oleo= 6.8
p1= int(input("Indique quantos pacotes de arroz está comprando: "))
p2= int(input("Indique quantos pacotes de feijão está comprando: "))
p3= int(input("Indique quantas garrafas de óleo está comprando: "))
calca = p1*arrz
calcf = p2*fei
calco = p3*oleo
calct = calca+calcf+calco
print(f"O valor do arroz é de R${round(calca, 2)}, o valor do feijão é R${round(calcf, 2)}, o valor do óleo é R${round(calco, 2)} e o total fica R${round(calct, 2)}")