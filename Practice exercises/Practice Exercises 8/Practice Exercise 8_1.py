# Zet beide trajecten allebei in een set met de namen “bruin” en “groen”
# Print daarna eerst met een set-functie welke plaatsen in
# beide trajecten worden aangedaan (de overeenkomst).
# Gebruik vervolgens opnieuw een set-functie om te printen
# hoe het traject “bruin” verschilt van het traject “groen”. Je
# moet dan dus op het scherm zien welke plaatsen van
# traject “bruin” ze niet allebei aandoen!
# Print ook alle stations op beide trajecten uit. Print elk
# station maar 1! Gebruik weer een set-functie!


bruin = {'Boxtel', 'Best','Beukenlaan','Eindhoven',"Helmond 't hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best','Beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}

print(bruin & groen)
print(bruin - groen)
print(bruin | groen)