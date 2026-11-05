# okay, alors en gros, si l'etudiant a une note > 40, 
# nous regardons le prochain nombre, 
# si le prochain nombre est un multiple de 5 
# et que la difference est <3, 
# alors on arrondit au prochain nombre multiple de 5

note_etud = input("Veuillez entrer les notes des etudiants : ").split()
resultat = []
#print(note_etud)

def notes(liste):
    liste_finale = []
    for a in liste:
        a = int(a)
        if a >= 40:
            for i in range(a+1,100):
                if (i%5)==0 and (i-a)<3:
                    a = i
                    #liste_finale.append(a)

        else:
            print("L'eleve a echoue! Il faut repasser le test.", a)
    
        liste_finale.append(a)

    return liste_finale

resultat = notes(note_etud)
print("Le resultat des notes est : ", resultat)