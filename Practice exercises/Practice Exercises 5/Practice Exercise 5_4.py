# Bij een marathonwedstrijd worden bij een controlepost alle voorbijkomende hardlopers genoteerd.
# De gegevens van elke hardloper worden in het bestand hardlopers.txt opgeslagen. Schrijf een
# programma waarmee een tekstbestand wordt aangemaakt (als het bestand nog niet bestaat) of
# aangevuld (gebruik de append-mode) met de gegevens van één hardloper (inlezen van toetsenbord).

import datetime

def toevoegen(hardloper):
    hardlopers = open('hardlopers.txt', 'a')
    vandaag = datetime.datetime.today()
    addition = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    hardlopers.write('\n')
    hardlopers.write(addition)
    hardlopers.write(', ')
    hardlopers.write(hardloper)
    hardlopers.close()

toevoeginput = input('Geef de naam van de hardloper: ')
toevoegen(toevoeginput)
