# Final Assignment: Bagagekluizen

def toon_aantal_kluizen_vrij():
    kluizen = open('kluizen.txt','r')
    aantalKluizen = kluizen.read()
    kluizen.close()

    totaalKluizen = aantalKluizen.split('\n')

    if len(totaalKluizen) == 12:
        print('Alle kluizen zijn in gebruik')
    else:
        print('Er zijn nog {} kluizen vrij'.format(12 - len(totaalKluizen)))

def nieuwe_kluis():
    nummerlijst = [1,2,3,4,5,6,7,8,9,10,11,12]
    kluizen = open('kluizen.txt', 'r')
    aantalKluizen = kluizen.read()
    kluizen.close()

    totaalKluizen = aantalKluizen.split('\n')

    for nummers in totaalKluizen:
        kluisnummers = nummers.split(';')
        if int(kluisnummers[0]) in nummerlijst:
            nummerlijst.remove(int(kluisnummers[0]))
    if len(nummerlijst) == 0:
        print('Er zijn geen kluizen vrij')
    else:
        wachtwoord = input('Geef een code voor uw kluis op(minimaal 4 tekens): ')
        while len(wachtwoord) < 4:
            print('\nDit wachtwoord is te kort, u moet minimaal 4 tekens gebruiken.')
            wachtwoord = input('Geef een code voor uw kluis op(minimaal 4 tekens): ')
        kluisnummer = nummerlijst[0]
        ontvangenKluis = '\n{};{}'.format(kluisnummer,wachtwoord)
        schrijven = open('kluizen.txt', 'a')
        schrijven.write(ontvangenKluis)
        schrijven.close()
        print('\nU heeft kluisnummer {} ontvangen'.format(kluisnummer))

def kluis_openen():
    kluisnummer = (input('Geef uw, kluisnummer op: '))
    kluiscode = input('Geef uw kluiscode op: ')
    kluisnc = kluisnummer()+';'+kluiscode()

    kluizen = open('kluizen.txt', 'r')
    aantalKluizen = kluizen.read()
    kluizen.close()

    totaalkluizen = aantalKluizen.split('\n')

    if kluisnc in totaalkluizen:
        print('dit is de correcte combinatie, uw kluis is open')
    else:
        print('Dit is de foute combinatie, probeer het opnieuw')

def kluis_teruggeven():
    pass


def keuzemenu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    print('4: Ik geef mijn kluis terug')
    print('5: Ik wil stoppen')

    print()
    optiekeuze = int(input('Wat wilt u doen? (geef nummer op)'))
    print()

    while optiekeuze < 5:
        if optiekeuze == 1:
            toon_aantal_kluizen_vrij()
            print()
            print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
            print('2: Ik wil een nieuwe kluis')
            print('3: Ik wil even iets uit mijn kluis halen')
            print('4: Ik geef mijn kluis terug')
            print('5: Ik wil stoppen')
            print()
            optiekeuze = int(input('Wat wilt u doen? (geef nummer op)'))
            print()

        elif optiekeuze == 2:
            nieuwe_kluis()
            print()
            print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
            print('2: Ik wil een nieuwe kluis')
            print('3: Ik wil even iets uit mijn kluis halen')
            print('4: Ik geef mijn kluis terug')
            print('5: Ik wil stoppen')
            print()
            optiekeuze = int(input('Wat wilt u doen? (geef nummer op)'))
            print()

        elif optiekeuze == 3:
            kluis_openen()
            print()
            print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
            print('2: Ik wil een nieuwe kluis')
            print('3: Ik wil even iets uit mijn kluis halen')
            print('4: Ik geef mijn kluis terug')
            print('5: Ik wil stoppen')
            print()
            optiekeuze = int(input('Wat wilt u doen? (geef nummer op)'))
            print()

        elif optiekeuze == 4:
            print('deze optie was optioneel en heb ik op dit moment niet gedaan')
            print()
            print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
            print('2: Ik wil een nieuwe kluis')
            print('3: Ik wil even iets uit mijn kluis halen')
            print('4: Ik geef mijn kluis terug')
            print('5: Ik wil stoppen')
            print()
            optiekeuze = int(input('Wat wilt u doen? (geef nummer op)'))
            print()
    print('Wij wensen u een goede dag')

keuzemenu()