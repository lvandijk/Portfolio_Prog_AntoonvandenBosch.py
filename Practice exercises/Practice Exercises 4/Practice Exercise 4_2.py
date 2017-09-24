# Practice Exercise 4_2 (functie met list-parameter)
# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst. Ga ervan uit dat dit een list is
# met integers. De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn!

def som(getallenlijst):
    optellen = sum(getallenlijst)
    return optellen

print(som(getallenlijst=[1,2,3,4,5,6]))