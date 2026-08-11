altura=float(input("Digite sua altura em metros"))
sexo=input("Digite seu sexo (M para masculino e F para feminino) :")

def _imc(altura, sexo):
    if sexo == "M":
        peso= (72.7*altura)-58
        print(peso)
    else:
        peso= (62.1*altura)-44.7
        print(peso)

_imc(altura, sexo)