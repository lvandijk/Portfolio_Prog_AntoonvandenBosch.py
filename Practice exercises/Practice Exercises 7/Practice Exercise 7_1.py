getallenlijst = []
totaalgetal = 0
while True:
    getal = eval(input('Geef een getal: '))
    if int(getal) == 0:
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallenlijst), totaalgetal))
        break
    getallenlijst.append(int(getal))
    totaalgetal += int(getal)