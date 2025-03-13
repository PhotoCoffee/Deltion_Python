# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
from modules import csv

persons = []
for line in open("personen.csv", 'rt'):
    lst = csv.sanitize(line)
    person = csv.create_person(lst)
    person = csv.add_fullname(person)
    persons.append(person)

# Filter persons based on the first letter of a specified field
letter = input("Enter a letter to filter: ").strip().lower()
field = input("Enter the field to filter by: ").strip().lower()

filtered_persons = csv.do_filter(persons, letter, field)

csv.print_persons(filtered_persons)