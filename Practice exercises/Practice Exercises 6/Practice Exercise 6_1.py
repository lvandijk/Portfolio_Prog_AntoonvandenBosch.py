def seizoen(maand):
    if maand == 12 or maand <3:
        print('het is winter')
    elif maand ==3 or maand < 6:
        print('het is lente')
    elif maand ==6 or maand < 9:
        print('het is zomer')
    elif 9 == maand or maand < 12:
        print('het is herfst')

print('december t/m februari')
seizoen(12)
seizoen(1)
seizoen(2)
print()
print('maart t/m mei')
seizoen(3)
seizoen(4)
seizoen(5)
print()
print('juni t/m augustus')
seizoen(6)
seizoen(7)
seizoen(8)
print()
print('september t/m november')
seizoen(9)
seizoen(10)
seizoen(11)