#Exercício 1
def soma(n):
    if n ==0:
        return 0
    else:
        return n + soma(n-1)


#Exercício 2
def potencia(n,b):
    if b == 0:
        return 1
    else :
        return n* potencia(n,b-1)

#Exercício 3
# def busca(lista,param):
#     if len(lista)==0:
#         return False
#     elif lista[0] == param:
#         return True
#     else:
#         busca(lista[1:],param)

#Exercício 4
def busca(lista,param):
    if len(lista)==0:
        return 0
    else:
        if lista[0] == param:
            return 1+ busca(lista[1:],param)
        else:
            return busca(lista[1:],param)
print(busca([3,4,6,5,4,7,3,5,5,10],3))
#Exercício 5
def mdc(x,y):
    if x>=y and x % y ==0:
        return y
    elif x<y:
        return mdc(y,x)
    else:
        return mdc(y, x%y)

