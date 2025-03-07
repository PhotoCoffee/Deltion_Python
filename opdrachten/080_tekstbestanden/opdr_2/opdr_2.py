# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
getal = random.randint(1, 99)
gok = 0
aantal_pogingen = 0

while gok != getal:
    aantal_pogingen += 1

#Sluit het programma als er iets anders dan een geldig getal wordt ingevoerd
    try: 
        gok = int(input('Raad het getal tussen 1 en 100: '))
    except ValueError:
        print('Dat is geen geldig getal.')
        exit()
#Einde van de try-except

#Sluit het programma als het getal buiten de range van 1 tot 100 ligt
    if gok <= 0:
        print('Het getal moet groter zijn dan 0.')
        exit()
    if gok >= 100:
        print('Het getal moet lager zijn dan 100.')
        exit()

#Einde

#Vergelijk gok met getal
    if gok < getal:
        print('Het getal is hoger dan ' + str(gok) +'. Probeer het opnieuw!')
        
    elif gok > getal:
        print('Het getal is lager dan ' + str(gok)+'. Probeer het opnieuw!')


print('Correct! Het getal was ' + str(getal) + '. Je hebt ' + str(aantal_pogingen) + ' keer gegokt.')