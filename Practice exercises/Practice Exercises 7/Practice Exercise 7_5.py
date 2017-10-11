def namen():
    namenlijst = []
    naamcounter = {}

    naam = input('Volgende naam: ').capitalize()
    while naam != '':
        namenlijst.append(naam)
        naam = input('Volgende naam: ').capitalize()

    for namen in namenlijst:
        if namen in naamcounter:
            naamcounter[namen] += 1
        else:
            naamcounter[namen] = 1

    for items in naamcounter:
        if naamcounter.get(items) > 1:
            print('Er zijn {} studenten met de naam {}'.format(naamcounter.get(items), items))
        else:
            print('Er is {} student met de naam {}'.format(naamcounter.get(items), items))

namen()