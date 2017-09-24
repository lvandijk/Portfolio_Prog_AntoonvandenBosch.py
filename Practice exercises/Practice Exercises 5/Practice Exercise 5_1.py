# Practice Exercise 5_1 (formatting)
# Schrijf een functie convert() waar je een temperatuur in graden Celsius (als parameter van deze
# functie) kunt omzetten naar graden Fahrenheit. Je kunt de temperatuur in Fahrenheit berekenen met
# de formule T(°F) = T(°C) × 1.8 + 32. Dus 25 °C = 25 * 1.8 + 32 = 77 °F.
# Schrijf nu ook een tweede functie table() waarin je met een for-loop van -30 °C t/m 40 °C in stappen
# van 10 graden de temperatuur in Fahrenheit print

def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def table():
    print('  F        C')
    temperatuur = '{:5.1f} {:8.1f}'
    for c in range(-30, 41, 10):
        print(temperatuur.format(convert(c), c))

table()