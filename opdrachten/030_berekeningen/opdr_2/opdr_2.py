# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
try:
    c = int(input('Geef een temperatuur in graden Celcius: '))
    f = int(input('Geef een temperatuur in graden Farenheit: '))

except ValueError:
    print('Dat is geen temperatuur!')
    exit()

Celcius2Farenheit = (c * 9/5) + 32
Farenheit2Celcius = (f - 32) * 5/9

print(f'{c} graden Celcius is gelijk aan {round(Celcius2Farenheit,2)} graden Farenheit')
print(f'{f} graden Farenheit is gelijk aan {round(Farenheit2Celcius, 2)} graden Celcius')