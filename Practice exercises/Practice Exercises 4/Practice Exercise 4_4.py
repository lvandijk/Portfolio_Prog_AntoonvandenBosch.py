# Practice Exercise 4_4 (functie met if)
# Schrijf (en test) een functie new_password() die 2 parameters heeft: oldpassword en newpassword.
# De return-waarde is True als het nieuwe password voldoet aan de eisen. Het nieuwe password wordt
# alleen geaccepteerd als het verschilt van het oude password èn als het minimaal 6 tekens lang is. Als
# dat niet zo is, is de return-waarde False.

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword)>=6:
        return True
    else:
        return False

print(new_password('test', 'test123'))  #test waar nieuwe wachtwoord anders is dan het oude wachtwoord en meer dan 6 tekens heeft = True
print(new_password('test', 'test'))     #test waar nieuwe wachtwoord gelijk is dan het oude wachtwoord = False
print(new_password('test', 'test1'))    #test waar nieuwe wachtwoord anders is dan het oude wachtwoord, maar niet meer dan 6 tekens heeft = False
