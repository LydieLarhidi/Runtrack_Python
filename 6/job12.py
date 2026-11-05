def trier(liste):
    for i in range(len_scratch(liste)):
        for j in range(0, len_scratch(liste)-i-1):
            if liste[j] > liste[j+1]:
                a = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = a
            j+=1
        i+=1
    return liste

def len_scratch(mon_objet):
    compteur = 0
    for _ in mon_objet:
        compteur += 1
    return compteur

liste = input("veuillez entrer la liste : ").split()
L = trier(liste)
print(L)

#print(len_scratch(L))