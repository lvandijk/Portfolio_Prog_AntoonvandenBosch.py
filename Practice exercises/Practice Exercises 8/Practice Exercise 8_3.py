# Practice Exercise 8_3 (ascii)
# Als extra beveiliging wil de NS op haar E-ticket nog een unieke code afbeelden. Er is gekozen voor een
# hele eenvoudige beveiliging: Neem de naam van de gebruiker+beginstation+eindstation, vertaal elk
# karakter naar ASCII en maak die waarde 3 groter. De “a” wordt dus een “d”, de “b” wordt een “e”, etc.
# De “A” wordt een “D”, de “W” wordt een “Z”, etc. En de spatie “ ” wordt een “#” .
# Zorg ervoor dat je code maakt die deze uitvoer maakt op basis van de invoer van de gebruiker. Schrijf
# een functie: def code(invoerstring): die ieder teken van invoerstring omzet naar zijn
# rangordenummer met bibliotheekfunctie ord(), en – na er 3 bij te hebben opgeteld – die int-waarde
# weer terug vertaalt naar het bijbehorende ASCII-teken met bibliotheekfunctie chr().

def code(invoerstring):
    print(invoerstring)
    for letter in invoerstring:
        codenummer = ord(letter)
        codeletter = chr(codenummer+3)
        print(codeletter, end='')


zin = input('Geef gebruiker+beginstation+eindstation: ')
code(zin)