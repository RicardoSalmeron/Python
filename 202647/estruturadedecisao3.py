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
# abordagem de match case
match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7 :
        print("Sábado")

    case _: #equivale ao else
        print("Número inválido")