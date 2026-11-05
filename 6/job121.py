def trier(liste):
    i = 0
    while i < len_scratch(liste):
        j = 0
        while j < len_scratch(liste)-i-1:
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

# print(len_scratch(L))