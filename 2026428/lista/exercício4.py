maioresDe18=[]
nomes=[]
idades=[]
i=0
while i<=10:
    i = i + 1
    n=input("Digite um nome:")
    nomes.append(n)
    age=int(input("Digite uma idade"))
    idades.append(age)
    if age >= 18:
        maioresDe18.append(n)



    if i==10:
        break
print(f'Nomes: {nomes} '
      f'Idades: {idades}, '
      f'Maiores de 18: {maioresDe18}')
