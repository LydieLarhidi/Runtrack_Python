a = float(input("Valeur a : "))
b = float(input("Valeur b : "))
c = float(input("Valeur c : "))

if a==0 or b==0 or c==0:
    print("Tiangle pas possible!")
else:
    if a==b==c :
        print("Le triangle est equilateral !")
    elif a==b or a==c or b==c :
        print("Le triangle est isocele !")
    elif (a**2==b**2+c**2) or (c**2==b**2+a**2) or (b**2==a**2+c**2):
        print("Le triangle est rectangle !")
    else:
        print("Le triangle est quelconque !")
    
