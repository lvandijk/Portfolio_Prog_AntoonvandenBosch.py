# Practice Exercise 2_4 (Input/Output)
# Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt
# heeft en dat daarna het salaris uitprint

uurloon = float(input('Wat verdien je per uur:'))
aantaluur= int(input('hoeveel uur heb je gewerkt:'))
print(str(aantaluur)+' uur werken levert '+ str(uurloon*aantaluur)+' Euro op.')