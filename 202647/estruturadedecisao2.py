#Estrutura de Decisao
#if, then(:), else;
#igualdades (==) e desigualdades (>,<, >=, <=, !=)
#operadores lógicos - juntam duas ou mais comparações no mesmo if
#and (malvado), or (bonzinho), not (do contra)
#elif
#nada mais é que junção do else+if
titulo = 'Dia da semana'
print(f'{titulo:^30}')
numero = int(input("Escolha um número de 1 até 7: "))
# abordagem de elif
if numero == 1:
    print("Domingo")
elif numero == 2:
        print("Segunda")
elif numero == 3:
        print("Terça")
elif numero == 4:
        print("Quarta")
elif numero == 5:
        print("Quinta")
elif numero == 6:
        print("Sexta")
elif numero == 7:
        print("Sábado")

else:
    print("Número inválido")