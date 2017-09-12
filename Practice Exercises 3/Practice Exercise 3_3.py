# Practice Exercise 3_3: Pas de uitwerking van 3_2 aan en geef ook een melding als de gebruiker niet mag stemmen

leeftijd = int(input('Geef je leeftijd:'))
paspoort = str(input('Nederlands paspoort(ja/nee):'))

if leeftijd >= 18 and paspoort == 'ja' or paspoort == 'Ja' or paspoort == 'JA':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Sorry, maar je mag niet stemmen.')