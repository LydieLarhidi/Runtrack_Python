def liste_fruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    print(fruits)
    return fruits

liste = liste_fruits()
liste.insert(2,"mangue")
print(liste)
