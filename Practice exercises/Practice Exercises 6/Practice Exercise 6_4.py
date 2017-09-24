# Practice Exercise 6_4 (two-dimensional-lists)
# Van elke student worden 3 cijfers bijgehouden. In de lijst studentencijfers staan de gegevens van 4
# studenten. Schrijf code voor twee functies die het gemiddelde cijfer voor iedere student en het
# gemiddelde van alle studenten berekent. De eerste functie heeft als return-waarde een ééndimensionale-lijst
# met alle gemiddelden per student, en de tweede functie heeft als return-waarde
# een int-getal met het gemiddelde van alle studenten!

studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gemiddeldestudent = []
    for gemiddelde in studentencijfers:
        antwoord = sum(gemiddelde)/len(gemiddelde)
        gemiddeldestudent.append(antwoord)
    return gemiddeldestudent

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddeldestudent = []
    for gemiddelde in studentencijfers:
        antwoord = sum(gemiddelde)/len(gemiddelde)
        gemiddeldestudent.append(antwoord)
    return int(sum(gemiddeldestudent)//len(gemiddeldestudent))


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))