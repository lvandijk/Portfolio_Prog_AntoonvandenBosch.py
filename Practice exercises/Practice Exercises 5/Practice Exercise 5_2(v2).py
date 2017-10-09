klantnummer = open('kaartnummers.txt')
content = klantnummer.read()
klantnummer.close()

lijst = content.split('\n')

for items in lijst:
    itemcontent = items.split(', ')
    print('{} heeft kaartnummer: {}'.format(itemcontent[1], itemcontent[0]))