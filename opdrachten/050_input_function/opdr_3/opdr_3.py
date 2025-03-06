# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

tel = 1
automerken = []
while tel < 11:
    automerken.append(input(f'Noem een automerk {tel}/10: '))
    tel += 1

automerken.sort()
automerken.reverse()

print("In omgekeerd alfabetische volgorde is dat:")
print(automerken)