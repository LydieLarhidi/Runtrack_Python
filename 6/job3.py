def liste_fruits():
    fruits = ["pomme", "cerise", "orange"]
    return fruits

liste = liste_fruits()
#liste.append("Melon")
liste.insert(3,"Melon")
#liste.append("tarte")

print(liste)