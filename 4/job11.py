def time_to_text(temps):
    heures = temps//60
    minutes = temps%60
    return heures, minutes


temps = int(input("veuillez entrer le temps en minutes : "))
h, m = time_to_text(temps)

print(h," heures et", m, "minutes")

