# Practice Exercise 2_2: De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie, afhankelijk van de cijfers
# die een student haalt. Voor elk cijferpunt krijg je € 30,-. Voor een 1,0 krijgt je dus 30 euro, voor een 2,5
# krijgt je 75 euro en voor een 10,0 beloont de HU een student met € 300,-.
# Maak variabelen cijferICOR, cijferPROG en cijferCSN. Geef ze alle drie de waarde die jij verwacht dat
# je voor de betreffende vakken in blok 1 zult gaan halen. Maak nu vervolgens ook de volgende
# variabelen aan, en bereken de bijbehorende waarden m.b.v. een Python expressie:
# gemiddelde het gemiddelde van de variabelen cijferICOR, cijferPROG en cijferCSN.
# beloning de totale beloning voor deze drie cursussen.
# overzicht een string met een tekstuele omschrijving het gemiddelde en de beloning:
# 'Mijn cijfers (gemiddeld een 7.5) leveren een beloning van € 675.0 op!'
# Print tot slot variabele overzicht! Schrijf dit programma in een nieuw bestand, bijvoorbeeld pe2_2.py.

cijferCSN = 7
cijferICOR = 7
cijferPROG = 7

gemiddelde = (cijferCSN + cijferICOR + cijferPROG)/3
beloning = (cijferCSN*10) + (cijferICOR*10) + (cijferPROG*10)
overzicht = 'Mijn cijfers(gemiddeld een ' + str(gemiddelde)+') leveren een beloning van € '+ str(beloning) + ' op!'
print(overzicht)