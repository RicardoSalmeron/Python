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
# abordagem de if alinhados
if numero == 1: #como estamos comparando com igualdades
    #tanto faz comparar com o 1(domingo) primeiro
    #como com o 5(quinta)
    #é particularmente interessante utilizar o número mais escolhido na primeira comparação
    #para priorizar performance
    print("Domingo")
else:
    if numero == 2:
        print("Segunda")
    else:
            if numero == 3:
                print("Terça")
            else:
                if numero == 4:
                    print("Quarta")
                else:
                    if numero == 5:
                       print("Quinta")
                    else:
                        if numero == 6:
                            print("Sexta")
                        else:
                            if numero == 7:
                                print("Sábado")
                            else:
                                print("Número inválido")