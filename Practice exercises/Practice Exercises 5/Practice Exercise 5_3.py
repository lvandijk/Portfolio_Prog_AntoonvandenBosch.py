# Practice Exercise 5_3 (files lezen)
# Schrijf een programma dat het bestand kaartnummers.txt opnieuw opent en het aantal regels en het
# grootste kaartnummer in het bestand bepaalt. Print deze gegevens vervolgens uit:

klantnummer = open('kaartnummers.txt', 'r')
content = klantnummer.readlines()
klantnummer.close()

nummerlijst = []

for nummer in content:
    itemcontent = nummer.split(', ')
    nummerlijst.append(int(itemcontent[0]))

print('Deze file telt', len(content), 'regels')
print('het grootste kaartnummer is: {} en dat staat op regel {}'.format(max(nummerlijst),nummerlijst.index(max(nummerlijst))+1))