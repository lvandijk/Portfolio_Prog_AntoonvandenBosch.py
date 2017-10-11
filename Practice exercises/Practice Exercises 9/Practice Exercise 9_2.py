import datetime
import csv

bestand = 'inloggers.csv'

def csvmakenmetheader():
    'Schrijf een csv file met een header'
    with open(bestand, 'w', newline='') as inlogCSVfile:
        writer = csv.writer(inlogCSVfile, delimiter=';')
        writer.writerow(('datum en tijd','naam','voorletters','geboortedatum','email'))

def toevoegen():
    with open(bestand, 'a', newline='') as inlogCSVfile:
        writer = csv.writer(inlogCSVfile, delimiter=';')
        while True:
            naam = input("Wat is je achternaam? ")
            if naam.lower() == 'einde' or naam == '':
                break
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            vandaag = datetime.datetime.today()
            datum = vandaag.strftime("%a %d %B %Y at %H:%M")
            writer.writerow((datum,naam,voorl,gbdatum,email))

toevoegen()