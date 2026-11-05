val = int(input("entrez un chiffre : "))
chaine = input("entrez une chaine de caractere : ")

def len_scratch(mon_objet):
    compteur = 0
    for _ in mon_objet:
        compteur += 1
    return compteur


def my_long_word(x, texte):
    liste_mots = []
    mots = texte.split()

    for mot in mots :
        if len_scratch(mot) > x:
            liste_mots.append(mot)

    return liste_mots

mots = my_long_word(val, chaine)
print(mots)