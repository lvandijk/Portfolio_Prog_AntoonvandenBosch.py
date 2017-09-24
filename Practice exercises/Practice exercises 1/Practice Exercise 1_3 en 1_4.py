# Practice Exercise 1_3: Schrijf Python statements die het volgende doen:

# 1. Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b
a = 6
b = 7
print(a)
print(b)

# 2. Ken aan variabele c als waarde het gemiddelde van a en b toe.
c= (a+b)/2
print(c)

# 3. Ken aan variabele inventaris de een lijst van strings toe: ‘papier’, ‘nietjes’, en ‘pennen’.
inventaris=['papier', 'nietjes', 'pennen']
print(inventaris)

# 4. Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe
voornaam = 'Antoon'
tussenvoegsel = 'van den'
achternaam = 'Bosch'
print(voornaam)
print(tussenvoegsel)
print(achternaam)

# 5. Ken aan variabele mijnnaam de variabelen van opdracht 4 (met spaties er tussen) toe.
mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
print(mijnnaam)


# Practice Exercise 1_4: Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1_3 evalueren of:

# 1. 6.75 groter is dan a en kleiner b. antwoord: true
print(6.75 > a or 6.75 < b)

# 2. de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam. antwoord: False
print(len(inventaris) > len(mijnnaam)*5)

# 3. de lijst inventaris leeg is, of juist meer dan 10 items bevat. antwoord: False
print(len(inventaris)==0 or len(inventaris)==10)