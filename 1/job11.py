#job11

chaine = str(input("Ecrivez..."))
print(chaine)
i=0

for caractere in chaine:
    if caractere=='e':
        i+=1
        print("il y a ", i, " e dans la chaine de caracteres")
    else:
        print("il n'y a pas de e dans la chaine de caracteres")