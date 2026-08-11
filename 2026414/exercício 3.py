i=1
over18=0
under18=0
while i<=15:
    age= int(input("Digite uma idade: "))
    if age<18:
        under18= under18+1
    elif age>=18:
        over18= over18+1
    i+=1
    print(f"{under18}, {over18}")