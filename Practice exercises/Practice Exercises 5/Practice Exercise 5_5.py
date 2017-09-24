# Practice Exercise 5_5 (string functions)
# Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren. De functie
# berekent vervolgens de gemiddelde lengte van de woorden in de zin en print dit uit.

def gemiddelde(zin):
    woorden = zin.split()
    nummers = []
    for woord in woorden:
        nummers.append(len(woord))
    print('De gemiddelde lengte per woord is',sum(nummers)//len(nummers))

zininput = input('geef een zin: ')
gemiddelde(zininput)