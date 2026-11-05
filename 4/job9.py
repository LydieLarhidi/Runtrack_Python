def average(a,b,c):
    moyenne = (a+b+c)/3
    return moyenne

a = float(input("entrez note 1 : "))
b = float(input("entrez note 2 : "))
c = float(input("entrez note 3 : "))
moyenne_etudiant = average(a,b,c)

if moyenne_etudiant <= 20 and moyenne_etudiant >= 15 :
    print("Très bon élève!", moyenne_etudiant)
elif moyenne_etudiant < 15 and moyenne_etudiant >= 11 :
    print("Bon élève!", moyenne_etudiant)
elif moyenne_etudiant <=10 and moyenne_etudiant >= 8 :
    print("Élève moyen!", moyenne_etudiant)
else:
    print("Élève devant faire des efforts!", moyenne_etudiant)

