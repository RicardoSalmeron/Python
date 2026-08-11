def calcular_media(python:float, webdev:float, frontend:float):
    return (python+ webdev+frontend)/3

media = calcular_media(9,8,9.5)

print(f'Média:{media:.1f}')

# parametro default
def calcular_dissidio(salario:float, percentual:float=0.08)-> float:
    if percentual >1:
        percentual /= 100
    salario_aumento = salario * (1 + percentual)
    return salario_aumento