# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

try:
    a = int(input('Geef de lengte van de eerste zijde: '))
    b = int(input('Geef de lengte van de tweede zijde: '))
except ValueError:
    print('Dat is geen getal!')
    exit()
c = a**2 + b**2
print(f'De schuine zijde is {c**0.5}')