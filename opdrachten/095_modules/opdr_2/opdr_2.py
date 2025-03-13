# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

from modules import csv

persons = []
for line in open("personen.csv", 'rt'):
    lst = csv.sanitize(line)
    person = csv.create_person(lst)
    person = csv.add_fullname(person)
    person = csv.add_adres(person, lst[3])
    person = csv.add_postcode(person, lst[4])
    person = csv.add_woonplaats(person, lst[5])
    persons.append(person)

# Filter persons based on a specified field and value
veld = input("Waar wil je op zoeken? (voornaam, tussenvoegsel, achternaam, adres, postcode, woonplaats): ").strip().lower()
value = input("welke letter?: ").strip().lower()

filtered_persons = csv.do_filter(persons, value, veld)

csv.print_persons(filtered_persons)