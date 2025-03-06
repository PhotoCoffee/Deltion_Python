# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

try:
    inputage = int(input("Wat is je leeftijd? (in jaren) "))
except ValueError:
    print("Voer een getal in met nummers.")
    exit()

categorie = None
for key, (min_age, max_age) in leeftijd.items():
    if min_age <= inputage <= max_age:
        categorie = key


if categorie:
    korting = kortings_percentages[categorie]
    toegangsprijs = normale_toegangsprijs * (1 - korting / 100)
    print(f"U valt in de categorie '{categorie}' met een korting van {korting}%. U betaalt daarom €{toegangsprijs:.2f}.")
else:
    print("Geen geldige leeftijdscategorie gevonden.")