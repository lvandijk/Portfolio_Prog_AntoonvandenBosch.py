def inlezen_beginstation(stations):
    beginstation = input('Wat is je beginstation? : ')
    while True:
        if beginstation in stations:
            return stations[stations.index(beginstation)]
        else:
            beginstation = input('Wat is je beginstation? : ')

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Wat is je eindstation? : ')
    while True:
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                return stations[stations.index(eindstation)]
            else:
                print('Dit station is in de andere richting, geef een ander station op.')
                eindstation = input('Wat is je eindstation? : ')
        else:
            print('Deze trein komt niet in {}'.format(eindstation))
            eindstation = input('Wat is je eindstation? : ')

def omroepen_reis(stations, beginstation, eindstation):
    bs = stations.index(beginstation)
    es = stations.index(eindstation)
    print('\nHet beginstation {} is het {}e station in het traject.'.format(stations[bs], bs+1))
    print('Het eindstation {} is het {}e in het traject'.format(stations[stations.index(eindstation)], stations.index(eindstation)+1))
    print('De afstand bedraagt {} station(s)'.format(es-bs))
    print('De prijs van het kaartje is {} euro'.format((es-bs)*5))
    print('Je stapt in de trein in: {}'.format(beginstation))
    for i in range(bs, es-1):
        print(' - {}'.format(stations[i+1]))
    print('Jij stapt uit in: {}'.format(eindstation))

stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amerstam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond','Sittard','Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)