nb_marches = int(input("veuillez entrer le nombres de marches depuis le haut : "))
hauteur_marche = float(input("veuillez entrer la hauteur de chaque marche en cm : "))

def calculer_distance(nb_marches, haut_marche):
    distance = (((nb_marches*haut_marche)*5)*2)*7
    distance_m = (distance/100) + (distance%100)
    return distance_m

distance_m = calculer_distance(nb_marches, hauteur_marche)
print("Pour", nb_marches, "de", hauteur_marche, "cm, le gardien parcourt", distance_m, "m par semaine.")

