import csv

with open('gamers.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')

    nummerlijst = []
    datums = []
    naam = []
    for row in reader:
        nummerlijst.append(int(row[2]))
        datums.append(row[1])
        naam.append(row[0])


print("De hoogste score is: {} op {} behaald door {}".format(max(nummerlijst), datums[nummerlijst.index(max(nummerlijst))], naam[nummerlijst.index(max(nummerlijst))]))