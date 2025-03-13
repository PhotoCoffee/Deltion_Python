# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    conversion = km * 0.621371
    return(f"{km} kilometers = {conversion} miles")

def miles_naar_kilometers(miles):
    conversion = miles * 1.60934
    return(f"{miles} miles = {conversion} kilometers")

kilometers = 1223
miles = 867

print(kilometers_naar_miles(kilometers))
print(miles_naar_kilometers(miles))