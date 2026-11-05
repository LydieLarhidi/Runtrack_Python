# liste = ["Lydie", "Marie", "Dylan"]
# liste2 = ["Tristan", "Evan", "Enzo"]
# liste3 = ["Antoine", "Terrence", "Timeo"]

# liste_finale = [liste, liste2, liste3]
# #print(liste_finale)
# print(liste_finale[1])

# # for prenom in liste_finale:
# #     print(prenom)

# i = 0
# while i < len(liste_finale):
#     # print(liste_finale[i])
#     j = 0

#     while j < len(liste_finale[i]):
#         print(liste_finale[i][j])
#         j+=1 

#     # print(liste_finale[i])
#     i+=1

L = [float(x) for x in input("Veuillez entrer les nombres de la liste : ").split()]

for i in range(len(L)):
    if L[i] >= 0:
        L[i] = int(L[i] + 0.5)
    else:
        L[i] = int(L[i] - 0.5)

for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]

print(L)