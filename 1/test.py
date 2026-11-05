#job9
'''
nom = ['robe', 'chemise', 'pantalon', 'jupe', 'tshirt', 'chaussettes', 'veste']
prix = [15, 18, 22, 10, 7, 2, 41]
quantite = [10, 15, 35, 12, 40, 43, 17]
'''
robe = ['robe', 15, 10]
chemise = ['chemise', 18, 15]
pantalon = ['pantalon', 22, 35]
jupe = ['jupe', 10, 12]
tshirt = ['tshirt', 7, 40]
chaussettes = ['chaussettes', 2, 43]
veste = ['veste', 41, 17]

print(robe[1])
print("nom du produit = ", robe[0], "\n prix unitaire = ", robe[1], "\n quantité en stock = ", robe[2])

#--------------------#

produit = input("produit : ")
nb_achat = input("Veuillez entrer la quantité que vous souhaotez achter : ")
print("Vous voulez acheter ", nb_achat, produit)

if produit == "robe" : 
    robe[2] = robe[2]-nb_achat
    robe[1] += robe[1]*0.1 

if produit == "jupe" : 
    jupe[2] = jupe[2]-nb_achat
    jupe[1] += jupe[1]*0.1 

if produit == "pantalon" : 
    pantalon[2] = pantalon[2]-nb_achat
    pantalon[1] += pantalon[1]*0.1 

if produit == "chaussettes" : 
    chaussettes[2] = chaussettes[2]-nb_achat
    chaussettes[1] += chaussettes[1]*0.1 

if produit == "veste" : 
    veste[2] = veste[2]-nb_achat
    veste[1] += veste[1]*0.1 

if produit == "tshirt" : 
    tshirt[2] = tshirt[2]-nb_achat
    tshirt[1] += tshirt[1]*0.1 

if produit == "chemise" : 
    chemise[2] = chemise[2]-nb_achat
    chemise[1] += chemise[1]*0.1 


print("nom du produit = ", robe[0], "\n prix unitaire = ", robe[1], "\n quantité en stock = ", robe[2])
