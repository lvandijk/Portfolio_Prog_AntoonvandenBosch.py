# Practice Exercise 4_6 (functie met (im)mutable parameter)
# Schrijf (en test) functie wijzig() met één parameter: letterlijst. Zorg dat de functie de lijst leegt en de
# letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde!

def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

# functie moet met onderstaande code getest worden

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)