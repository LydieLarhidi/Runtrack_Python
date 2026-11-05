hauteur = int(input("Veuillez entrer la hauteur : "))

for ma_ligne in range(hauteur):
    if ma_ligne == 0:
        print(" " * (hauteur - 1) + "/\\")
    elif ma_ligne == hauteur - 1:
        print("/" + "_" * (2 * hauteur - 2) + "\\")
    else:
        print(" " * (hauteur - 1- ma_ligne) + "/" + " " * (2 * ma_ligne) + "\\")

