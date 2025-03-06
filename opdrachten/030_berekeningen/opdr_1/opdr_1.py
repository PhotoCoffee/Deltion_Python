# Opdracht 1 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

vrienden = {
"braldt" : 25,
"kevin" : 26,
"harm" : 29,
}

gemiddelde = sum(vrienden.values()) / len(vrienden)
totaal = sum(vrienden.values())
namen = vrienden.keys()

print('dit weten we over de vrienden:', end=' ')
for key in namen:
    print(key, end=' ')

print('\nDe totale waarde van alle leeftijden bij elkaar opgeteld = ', totaal)
print('De gemiddelde leeftijd van deze boys is: ', gemiddelde)