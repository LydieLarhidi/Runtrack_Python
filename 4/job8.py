def what_to_eat(type, season):
    match type:
        case "fruits" if season=="hiver" :
            print("orange,  mandarine et kiwi")
        case "fruits" if season=="ete" :
            print("Poire, fraise, cassis")
        case "legume" if season=="hiver" :
            print("carotte, topinambour, endive")
        case "legume" if season=="ete" :
            print("artichaut, aubergine,navet")

type = input("Veuillez entrer le type : ")
season = input("Veuillez entrer la saison : ")

what_to_eat(type, season)
