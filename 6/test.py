# liste = ["Lydie", "Marie", "Dylan", "Arthur", "Enzo"]
# print(liste[1])

# # i = 0
# # while i < len(liste):
# #     print(liste[i])
# #     i += 1

# for nom in liste:
#     print(nom)

# dictionnaire = {"nom" : ["Lydie", "Marie", "Dylan", "Arthur", "Enzo"],
#                 "age" : [10, 8, 24, 90, 18]}

# print(dictionnaire["nom"])
# print(dictionnaire["age"])


# dictionnaire1 = {"nom" : "Lydie",
#                 "age" : 10}

# print(dictionnaire1["nom"])
# print(dictionnaire1["age"])




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

sum_even = sum(x for x in L if x % 2 == 0)
print(sum_even)

for i in range(len(L)): 
    for j in range(i+1, len(L)): 
        if L[i] > L[j]: L[i], L[j] = L[j], L[i]
print(L)
