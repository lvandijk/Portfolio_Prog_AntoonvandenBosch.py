# Schrijf functie monopolyworp(), die een het gooien van twee dobbelstenen voor het spel Monopoly
# simuleert en afdrukt. Je mag nogmaals gooien als beide stenen dezelfde waarde hebben. Zorg dat de
# functie die worpen ook simuleert! Na driemaal dubbel moet de speler naar de gevangenis!


import random

def monopolyworp():
    dubbelcounter = 0
    while dubbelcounter < 3:
        nummerEen = random.randrange(1, 7)
        nummerTwee = random.randrange(1, 7)
        nummerDrie = random.randrange(1, 7)
        nummerVier = random.randrange(1, 7)
        nummerVijf = random.randrange(1, 7)
        nummerZes = random.randrange(1, 7)
        eersteworp = nummerEen + nummerTwee
        tweedeworp = nummerDrie + nummerVier
        derdeworp = nummerVijf + nummerZes

        if dubbelcounter == 0 and nummerEen == nummerTwee:
            print('{} + {} = {} (Dubbel!)'.format(nummerEen, nummerTwee, eersteworp))
            dubbelcounter += 1
        else:
            print('{} + {} = {}'.format(nummerEen, nummerTwee, eersteworp))
            break
        if dubbelcounter == 1 and nummerDrie == nummerVier:
            print('{} + {} = {} (Dubbel!)'.format(nummerDrie, nummerVier, tweedeworp))
            dubbelcounter += 1
        else:
            print('{} + {} = {}'.format(nummerDrie, nummerVier, tweedeworp))
            break
        if dubbelcounter == 2 and nummerVijf == nummerZes:
            print('{} + {} = {} (Naar de gevangenis!)'.format(nummerVijf, nummerZes, derdeworp))
            break
        else:
            print('{} + {} = {}'.format(nummerVijf, nummerZes, derdeworp))
            break

monopolyworp()