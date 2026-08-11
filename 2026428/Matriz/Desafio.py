from faker import Faker


fake= Faker()
names1 = []
names2 =[]
names3 =[]
names4 = []
i=0
while i < 12:
    names = fake.name

    if i < 3:
        names1.append(names)

    elif i < 6:
        names2.append(names)

    elif i < 9:
        names3.append(names)

    elif i < 12:
        names4.append(names)

    i=+1

matriz = [names1, names2, names3, names4]
print(matriz)