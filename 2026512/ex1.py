nota1=float(input("Digite a primeira nota"))
nota2=float(input("Digite a segunda nota"))

def _media(nota1, nota2):
    media= (nota1+nota2)/2
    if media<6:
        print("Você foi reprovado (SE FUDEU)")
    else:
        print("Aprovado")
_media(nota1, nota2)