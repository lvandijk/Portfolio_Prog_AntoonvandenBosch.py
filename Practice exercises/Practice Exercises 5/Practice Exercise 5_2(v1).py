# Practice Exercise 5_2 (files lezen)
# Maak met behulp van PyCharm (of Notepad) het bestand 'kaartnummers.txt', dat
# bestaat uit klantenkaartnummers en namen
# Schrijf een Python programma waarmee je het bestand opent, en splits elke regel op de komma

kaartnummer = open('kaartnummers.txt', 'w')
kaartnummer.write('325255, Jan Jansen\n')
kaartnummer.write('334343, Erik Materus\n')
kaartnummer.write('235434, Ali Ahson\n')
kaartnummer.write('645345, Eva Versteeg\n')
kaartnummer.write('534545, Jan de Wilde\n')
kaartnummer.write('345355, Henk de Vries\n')
kaartnummer.close()

klantnummer = open('kaartnummers.txt', 'r')
content = klantnummer.readline()
content2 = klantnummer.readline()
content3 = klantnummer.readline()
content4 = klantnummer.readline()
content5 = klantnummer.readline()
content6 = klantnummer.readline()
klantnummer.close()

lijst = content.strip().split(', ')
lijst2 = content2.strip().split(', ')
lijst3 = content3.strip().split(', ')
lijst4 = content4.strip().split(', ')
lijst5 = content5.strip().split(', ')
lijst6 = content6.strip().split(', ')

print(lijst[1], 'heeft kaartnummer:', lijst[0])
print(lijst2[1], 'heeft kaartnummer:', lijst2[0])
print(lijst3[1], 'heeft kaartnummer:', lijst3[0])
print(lijst4[1], 'heeft kaartnummer:', lijst4[0])
print(lijst5[1], 'heeft kaartnummer:', lijst5[0])
print(lijst6[1], 'heeft kaartnummer:', lijst6[0])