liste = input("Veuillez entrer les elements de la liste : ").split()

def my_sort(liste):
    #a = int(a)
    compteur = 0
    liste_triee = []
    for a in range(len(liste)-1):
        if liste[a] > liste[a+1]:
            liste[a], liste[a+1] = liste[a+1], liste[a]
            compteur += 1
        #liste_triee.append(a)

    return liste, compteur

liste_triee, compt = my_sort(liste)
print("Nombre total de coups necessaires pour trier la liste est ", compt)
print("Liste triee : ", liste_triee)

            
