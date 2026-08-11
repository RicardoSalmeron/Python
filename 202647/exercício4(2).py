letra= input("Informe uma letra: ").lower()
# if letra == "a" or letra == 'e' or letra == "i" or letra == "o" or letra == "u":
#     print("Vogal")
# else:
#     print("Consoante")

match letra:
    case 'a'|'e'|'i'|'o'|'u' :
        print("vogal")
    case _:
        print("consoante")