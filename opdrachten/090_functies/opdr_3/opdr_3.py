# Opdracht 1 functies
# Naam student:
# Groep:


def kubus_vol(m):
    volume = m ** 3
    return(f"De inhoud van deze kubus is: {volume}.")

def bol_vol(r):
    volume = (4/3) * 3.14159265358979323846 * r ** 3
    return(f"De inhoud van deze bol is: {volume}.")

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))