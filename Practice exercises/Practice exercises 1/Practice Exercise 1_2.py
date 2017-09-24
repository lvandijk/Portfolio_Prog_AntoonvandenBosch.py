# Practice Exercise 1_2: Schrijf en evalueer python expressies die de volgende vragen beantwoorden

# A. Hoeveel letters zitten er in 'Supercalifragilisticexpialidocious'? Antwoord: 34
a = len('Supercalifragilisticexpialidocious')
print(a)

# B. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor? Antwoord: True
b = 'ice' in 'Supercalifragilisticexpialidocious'
print(b)

# C. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'? Antwoord: True
c = len('Antidisestablishmentarianism') > len('Honorificabilitudinitatibus')
print(c)

# D. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian','Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst? Antwoord: Bartok komt als eerste, Buxtehude komt als laatste
componist = ['berlioz', 'borodin', 'brian', 'bartok', 'bellini', 'buxtuhude', 'bernstein']
componist.sort()
print(componist)