n = int(input("Veuillez entrer un entier supérieur à zéro : "))
liste = [1,2,3,4,5,6,7,8,9,10]
for j in range (1,n+1):
    for i in liste : 
        #print(j*i)
        #print("Table de multiplication de ",j, " :")
        print("",j,"x",i," = ",j*i)