#L = [1,2,3,4,5]
L = input("Entrez les valeurs successivement ... : ").split()
print("La liste est : ", L)
a = L[0]
L[0] = L[-1]
L[-1] = a
print("La nouvelle liste est : ", L)
