import csv

with open('artikelen.csv', 'r') as myCSVFile:

    reader = csv.DictReader(myCSVFile, delimiter=';')

    artikel = []
    prijs = []
    artikelnummer = []
    voorraad = []
    for row in reader:
        artikelnummer.append(int(row['Artikelnummer']))
        artikel.append(row['Naam'])
        prijs.append(float(row['Prijs']))
        voorraad.append(int(row['Voorraad']))

    print('Het duurste artikel is {0:} en die kost {1:.2f} Euro'.format(artikel[prijs.index(max(prijs))], max(prijs)))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(min(voorraad), artikelnummer[voorraad.index(min(voorraad))]))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(sum(voorraad)))