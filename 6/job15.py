L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def len_scratch(mon_objet):
    compteur = 0
    for _ in mon_objet:
        compteur += 1
    return compteur

for i in range(len_scratch(L)): 
    L[i] = int(L[i] + 0.5)
    for i in range(len_scratch(L)): 
        for j in range(i+1, len_scratch(L)): 
            if L[i] > L[j]: L[i], L[j] = L[j], L[i]

print("La liste arrondie et triee par ordre croissant est : ", L)