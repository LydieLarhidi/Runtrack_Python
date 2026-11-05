L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L = [x for i, x in enumerate(L) if x not in L[:i]]
print(L)


L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L1 = []

def len_scratch(mon_objet):
    compteur = 0
    for _ in mon_objet:
        compteur += 1
    return compteur 

i = 0
while i < len_scratch(L):
    if L[i] not in L1:
        L1.append(L[i])
    i+=1
print(L1)

