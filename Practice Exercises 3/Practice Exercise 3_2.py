# Practice Exercise 3_2: Je mag stemmen als je 18 of ouder bent èn in het bezit bent van een Nederlands paspoort. Schrijf een
# programma dat de leeftijd van de gebruiker vraagt en of diegene een Nederlands paspoort heeft (ja/nee).
# Als aan beide voorwaarden is voldaan, print dan dat de gebruiker mag stemmen!
# Voor deze opgave mag je daarom maximaal 1 keer een if-statement gebruiken.

leeftijd = int(input('Geef je leeftijd:'))
paspoort = str(input('Nederlands paspoort(ja/nee):'))

if leeftijd >= 18 and paspoort == 'ja' or paspoort == 'Ja' or paspoort == 'JA':
    print('Gefeliciteerd, je mag stemmen!')