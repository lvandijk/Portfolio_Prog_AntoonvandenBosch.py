# Practice Exercsie 6_2 Schrijf een nieuw programma waarin een list met minimaal 10 strings wordt ingelezen. Het programma
# plaatst alle vier-letter strings uit de ingelezen list in een nieuwe list en drukt deze af
# ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"] < voor copy paste convenience


woordenlijst = eval(input("Geef lijst met minimaal 10 strings: "))

vierletters = []
for woord in woordenlijst:
    if len(woord) == 4:
        vierletters.append(woord)

print('de nieuwe lijst met alle 4 letter strings is: ')
print(vierletters)