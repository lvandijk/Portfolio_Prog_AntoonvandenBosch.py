# Practice Exercise 6_5 (nested loop)
# Schrijf een programma met twee for-loops in elkaar (nested) om de tafels van 1 t/m 10 uit te printen.

for nummer1 in range(1, 11, 1):
    for nummer2 in range(1, 11, 1):
        print('{} x {} = {}'.format(nummer1, nummer2, nummer1*nummer2))
    print()