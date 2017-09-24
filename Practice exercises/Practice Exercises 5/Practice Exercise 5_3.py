# Practice Exercise 5_3 (files lezen)
# Schrijf een programma dat het bestand kaartnummers.txt opnieuw opent en het aantal regels en het
# grootste kaartnummer in het bestand bepaalt. Print deze gegevens vervolgens uit:

klantnummer = open('kaartnummers.txt', 'r')
content = klantnummer.readlines()
klantnummer.close()

print('Deze file telt', len(content), 'regels')
