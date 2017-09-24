# Practice Exercise 3_1: Schrijf een programma dat de gebruiker vraagt om de score van een multiplechoice toets. Het
# programma bepaalt of het resultaat voldoende is. Bij meer dan 15 punten is de deelnemer geslaagd!

score = int(input('Geef je score:'))

if score > 15:

    print('Gefeliciteerd!')
    print('Met een score van ' + str(score) + ' ben je geslaagd!')

# Als je de print opdrachten direct onder de if statement plaats dan krijg je een foutmelding