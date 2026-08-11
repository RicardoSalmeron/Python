i=1
interval=0
while i<=10:
    number=float(input("Digite um número: "))
    if 200>number>100:
        interval+=1
    i+=1
    print(f"{interval}")