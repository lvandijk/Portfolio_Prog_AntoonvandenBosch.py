# Practice Exercise 6_3 (lists)
# Gegeven is variabele invoer = "5-9-7-1-7-8-3-2-4-8-7-9". Schrijf een nieuw programma
# waarin je deze variabele splitst in een lijst van getallen en print de gesorteerde lijst. Bepaal en print na
# het opsplitsen de grootste waarde, kleinste waarde, aantal getallen, de som en het gemiddelde!

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
nummerlijst = invoer.split('-')
nummerlijst = [int(i) for i in nummerlijst]
print(nummerlijst)
nummerlijst.sort()
print('Gesorteerde lijst van ints: ', nummerlijst)
print('Grootste getal: {} en kleinste getal {}'.format(max(nummerlijst), min(nummerlijst)))
print('Aantal getallen: {} en som van getallen {}'.format(len(nummerlijst), sum(nummerlijst)))
print('Gemiddelde: {}'.format(sum(nummerlijst)/len(nummerlijst)))