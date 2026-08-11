lados= int(input("Digite o números de ladso da forma: "))

def _dizerPoligonos(lados):
    if lados == 3:
        print("triângulo")
    elif  lados == 4:
        print("Quadrilátero")
    elif lados == 5:
        print("Pentágono")
    else:
        print("Número inválido")

_dizerPoligonos(lados)