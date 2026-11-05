#L = [1,2,3,4,5]
L = input("Entrez les valeurs successivement ... : ").split()
print("La 2e valeur de la liste est : ", L[1])
def remplacer(liste):
    liste[3] = int(liste[2]) + int(liste[4])

# L[3] = L[2]+L[4]
remplacer(L)
print("La nouvelle liste est : ", L)
print("La derniere valeur de la liste est ", L[-1])