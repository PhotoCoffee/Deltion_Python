def sanitize(line):
   # kleine letters maken en spaties voor en na het woord weghalen
   new_lst = []
   lst = line.split(',')
   for item in lst:
       new_lst.append(item.lower().rstrip().strip())
   return new_lst

def create_person(lst):
    person = {"voornaam": "", "tussenvoegsel": "", "achternaam": ""}
    person["voornaam"] = lst[0]
    person["tussenvoegsel"] = lst[1]
    person["achternaam"] = lst[2]
    return person

def add_fullname(person):
    if person["tussenvoegsel"] == "":
        person['full_name'] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person['full_name'] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person

def add_adres(person, adres):
    person['adres'] = adres
    return person

def add_postcode(person, postcode):
    person['postcode'] = postcode
    return person

def add_woonplaats(person, woonplaats):
    person['woonplaats'] = woonplaats
    return person

def print_persons(persons, filter=["full_name"]):
    counter = 0
    for person in persons:
        counter += 1
        for attr in filter:
            print(person[attr].title(), end=" ")
        print(end="\n")
    print(f"Er zijn in totaal {counter} personen")

def do_filter(persons, letter, field):
    filtered = []
    for person in persons:
        if person[field].startswith(letter):
            filtered.append(person)
    return filtered
