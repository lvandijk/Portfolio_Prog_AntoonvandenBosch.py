# Final Assignment: NS-functies
# De NS heeft standaardtarieven voor treinreizen, maar onder sommige omstandigheden krijgen
# reizigers korting. Bijvoorbeeld omdat ze in een bepaalde leeftijdscategorie vallen. In deze opdracht
# maak je twee functies: standaardtarief(..) en ritprijs(..). De eerste functie bepaalt het standaardbedrag
# voor een bepaalde rit. De tweede functie maakt hier gebruik van, maar bepaalt zelf ook nog welke
# kortingen van toepassing zijn en levert als return-waarde de definitieve prijs.

def standaardprijs(afstandKM):
    if afstandKM < 0:
        return 0
    else:
        if afstandKM > 50:
            return 15+0.60*afstandKM
        else:
            return 0.80*afstandKM


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)
    if weekendrit == 'ja':
        if leeftijd < 12 or leeftijd >=65:
            return standaardprijs(afstandKM)*0.65
        else:
            return standaardprijs(afstandKM)*0.60
    else:
        if leeftijd < 12 or leeftijd >=65:
            return standaardprijs(afstandKM)*0.70
        else:
            return standaardprijs(afstandKM)

print('testleeftijd: 11, 3 keer weekendrit, 3 keer werkdagrit, afstanden -10KM, 10KM en 60KM')
print('€' , ritprijs(11,'nee',-10), '€' , ritprijs(11,'nee',10), '€' , ritprijs(11,'nee',60))
print('€' , ritprijs(11,'ja',-10), '€' , ritprijs(11,'ja',10), '€' , ritprijs(11,'ja',60))
print('testleeftijd: 12, 3 keer weekendrit, 3 keer werkdagrit, afstanden -10KM, 10KM en 60KM')
print('€' , ritprijs(12,'nee',-10), '€' , ritprijs(12,'nee',10), '€' , ritprijs(12,'nee',60))
print('€' , ritprijs(12,'ja',-10), '€' , ritprijs(12,'ja',10), '€' , ritprijs(12,'ja',60))
print('testleeftijd: 64, 3 keer weekendrit, 3 keer werkdagrit, afstanden -10KM, 10KM en 60KM')
print('€' , ritprijs(64,'nee',-10), '€' , ritprijs(64,'nee',10), '€' , ritprijs(64,'nee',60))
print('€' , ritprijs(64,'ja',-10), '€' , ritprijs(64,'ja',10), '€' , ritprijs(64,'ja',60))
print('testleeftijd: 65, 3 keer weekendrit, 3 keer werkdagrit, afstanden -10KM, 10KM en 60KM')
print('€' , ritprijs(65,'nee',-10), '€' , ritprijs(65,'nee',10), '€' , ritprijs(65,'nee',60))
print('€' , ritprijs(65,'ja',-10), '€' , ritprijs(65,'ja',10), '€' , ritprijs(65,'ja',60))
