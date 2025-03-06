# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
def gastenlijst():
    print("Restaurantgasten")
    for i in gasten:
        print (i)
    print("\n")

gasten = ["Ik", "Paul", "Kees", "Marie", "Hilda"]
gastenlijst()

print("MARIE belt af!")
gasten.remove("Marie")
gastenlijst()

print("George wil mee, maar hij wil naast Kees zitten")
gasten.insert(3, "George")
gastenlijst()