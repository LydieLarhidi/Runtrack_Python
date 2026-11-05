L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def maximum_fonction(L):
    maximum = 0
    for i in L:
        if i > maximum:
            maximum = i
    return maximum

def minimum_fonction(L):
    minimum = 100
    for i in L:
        if i < minimum:
            minimum = i
    return minimum



for i in L:
    max_valeur = maximum_fonction(L)
    min_valeur = minimum_fonction(L)

print("Le max est : ", max_valeur)
print("Le min est : ", min_valeur)