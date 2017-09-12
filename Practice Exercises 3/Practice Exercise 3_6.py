# Practice Exercise 3_6:
# Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint, maar alleen als het
# een klinker is ('aeiou'). Gebruik string s = "Guido van Rossum heeft programmeertaal
# Python bedacht."

s = 'Guido van Rossum heeft programmeertaalPython bedacht.'

for klinker in s:
    if klinker in 'aeoiu':
        print(klinker)