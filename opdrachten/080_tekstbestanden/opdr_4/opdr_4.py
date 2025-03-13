# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
bestand = open("feest.txt", "a")
bestand.write("----  \n")
vragenlijst = ['1. Wat is je voornaam?', '2. Wat is je achternaam?', '3. Wat neem je mee aan drank?', '4. Wat neem je mee om te eten?']
for i in range(4):
    bestand.write(input(vragenlijst[i] + ' '))
    bestand.write("\n")


print('Bedankt voor het invullen!') 
print('See you at the party.') 