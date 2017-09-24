# Practice Exercise 1_6: Het bereik van een lijst is het verschil tussen het grootste en het kleinste getal. Schrijf een Python
# expressie die het bereik van een lijst berekent. Als bijvoorbeeld variabele list bestaat uit de getallen 3,
# 7, -2 en 12, dan moet de expressie evalueren naar 14 (verschil tussen 12 en -2). Zorg dat de expressie
# altijd werkt, ook al bestaat de lijst uit andere waarden!

verschil = [3, 7, -2, 12]
print(verschil)

print(max(verschil)-min(verschil))