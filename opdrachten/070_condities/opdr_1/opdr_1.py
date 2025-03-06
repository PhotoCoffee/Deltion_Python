# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

my_list = []

for i in range(1,11):
    my_list.append(i)
    if i > 4: print(i)

print('maar dat is niet de output zoals beschreven in de opdracht, dat moet ingewikkelder')
my_list2 = []
for i in range(1,11):
    if i > 4:
        my_list2.append(i)

print(my_list2)
print('dit is de output maar de lijst bevat nu niet 1/10')