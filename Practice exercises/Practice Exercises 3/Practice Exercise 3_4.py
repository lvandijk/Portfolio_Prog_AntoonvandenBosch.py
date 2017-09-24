# Practice Exercise 3_4: Schrijf een for-loop die over een lijst met strings itereert, en van elk woord de eerste twee karakters
# print. De lijst [ ‘maandag’, ‘dinsdag’, ‘woensdag’ ] zou dus moeten resulteren in:
# ma
# di
# wo

lijst = ['maandag', 'dinsdag', 'woensdag']

for karakter in lijst:
    print(karakter[0]+karakter[1])