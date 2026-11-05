def metier(language ):
    match language :
        case "JavaScript":
            print("tu es un développeur Web!")
        case "Python":
            print("tu es un développeur IA!")
        case "Java":
            print("tu es un développeur logiciel!")
        case "React Native":
            print("tu es un développeur mobile!")
        case _:
            print("un jour, je serai le meilleur développeur…!")

language = input("quel est votre language de programmation ?")
metier(language)