# okay, alors en gros, si l'etudiant a une note > 40, 
# nous regardons le prochain nombre, 
# si le prochain nombre est un multiple de 5 
# et que la difference est <3, 
# alors on arrondit au prochain nombre multiple de 5

note_etud = int(input("Veuillez entrer la note de l'etudiant : "))

def notes(a):
    if a >= 40:
        for i in range(a+1,100):
            if (i%5)==0 and (i-a)<3:
                a = i

    else:
        print("L'eleve a echoue! Il faut repasser le test.")

    return a

resultat = notes(note_etud)
print(resultat)