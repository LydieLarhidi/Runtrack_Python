message = input("Veuillez entre le message : ")
decalage = int(input("Veuillez entrer le decalage : "))

def decaler(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mess_decale = ""

    for lettre in message:
        if lettre in alphabet:
            place_lettre = (alphabet.index(lettre) + decalage)%26
            print(alphabet.index(lettre)) #fonction index() => documentation, pour renvoyer l'indice dans une liste ou chaine de caractere
            mess_decale += alphabet[place_lettre]
    return mess_decale

resultat = decaler(message, decalage)
print(resultat)