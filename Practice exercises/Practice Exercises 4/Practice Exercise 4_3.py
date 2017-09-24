# Practice Exercise 4_3 (functie met if)
# Schrijf (en test) de functie lang_genoeg() die voor Efteling-attracties bepaalt of een gebruiker in een
# attractie mag. De functie heeft één parameter, namelijk de lengte van de gebruiker in centimeters. Als
# de gebruiker 120 centimeter of langer is de return-waarde van de functie “Je bent lang genoeg voor
# de attractie!”, anders is de melding “Sorry, je bent te klein!”.

def lang_genoeg(lengte):
    if lengte >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein")

lang_genoeg(120)

lang_genoeg(80)