kosten = 4356
try:
    personen = int(input('Geef aantal personen op: '))
    if personen < 0:
        print('Geen negatieve getallen!')
    else:
        print('De kosten per persoon zijn: {}'.format(kosten/personen))
except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except ValueError:
    print('Gebruik cijfers!')
except:
    print('Onjuiste invoer!')