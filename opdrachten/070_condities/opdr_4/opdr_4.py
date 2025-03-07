# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [key[0] for key in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

for key, prijs in toppings:
    if keuze.lower() == key:
        print(f"Je hebt gekozen voor {key} en dat kost €{prijs:.2f}.")

if keuze.lower() not in beschikbare_toppings:
    print("Deze topping is niet beschikbaar.")
    exit()
# Hier de rest van jouw code...