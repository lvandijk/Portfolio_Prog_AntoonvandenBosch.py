# Practice Exercise 10_2 (Namespaces)
# In onderstaande programma’s wordt verkeerd gebruik gemaakt van namespaces. Verbeter de code!

# verbetering: globale b gebruikt
b = 7
def verdubbelB():
    global b
    b = b + b
verdubbelB()
print(b)

# verbetering: de time functie geimport
import time

print(time.strftime(("%H:%M:%S")))

# verbetering: def g boven de print geplaatst zodat ie gebruikt word
def f(y):
    return 2*y + 1

def g(x):
    return 5 + x + 10

print(f(3)+g(3))