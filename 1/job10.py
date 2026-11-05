#job10
init_montant = int(input("investissement = "))
taux = float(input("taux de rendemetn annuel (en %) = ")) 
gain_annuel = init_montant*taux
print("Le gain annuel est de ", gain_annuel, "euros")

nv_capital = init_montant + 5000
nv_gain = nv_capital*0.02

print("Le nouveau gain est de ", nv_gain, "euros")

montant_total = gain_annuel+nv_capital+nv_gain
print("Le montant total est de ", montant_total, "euros")

retrait = montant_total*0.1
reste_total = montant_total-retrait

print("Il reste du coup de l'investissement apres le retrait de 10 pourcent de la somme totale ", reste_total, "euros")
nv_rendement = 0.01

nv_nv_gain = reste_total*nv_rendement

print("le gain final apres 1\% de rendement est de ", nv_nv_gain, "euros")