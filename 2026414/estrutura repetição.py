from itertools import repeat

title = "Estrutura de repetição"
print(f'{title:^30}')

#se nós quisermos realizar a tabuada do 3 teriamos que fazer a mesma operação 10 vezes

number= int(input("Escolha um número para a tabuada: "))
print(f"{number} X 1 = {number*1}")

#while
# a repetição está estruturada enquanto a comparação for verdadeira
i = 1
question= "yes"
while question == "sim" or question == "yes":
    while i<=10:
        multiplication = i * number
        print(f"{number} x {i} = {number*i}")
        i+= 1
        if i>10:
            i = 1
            number = number + 1
            question = input("Quer calcular a próxima? ").lower()


