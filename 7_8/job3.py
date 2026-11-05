taille = int(input("Veuillez entrer la taille du tapis : "))

def creer_tapis(n):
    print("+" + "-"*n + "+")
    for i in range(n):
        print("|" + "#"*(n-i-1) + " " + "#"*(i) + "|") # +2 sinon c'est decale, meme avec +1

    print("+" + "-"*n + "+")

creer_tapis(taille)