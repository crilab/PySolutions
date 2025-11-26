pet_owners = [
    { 'name': 'Anna', 'id': 'aa' },
    { 'name': 'Lars', 'id': 'bb' },
    { 'name': 'Eva', 'id': 'cc' }
]

pets = [
    { 'name': 'Doris', 'owner_id': 'bb' },
    { 'name': 'Molly', 'owner_id': 'cc' },
    { 'name': 'Stampe', 'owner_id': 'aa' },
    { 'name': 'Luna', 'owner_id': 'bb' },
    { 'name': 'Pelle', 'owner_id': 'aa' }
]

pet_owner_name = input('pet owner name > ')

# DIN KOD NEDAN

def get_owner_id(owner_name):
    for pet_owner in pet_owners:
        if pet_owner['name'] == owner_name:
            return pet_owner['id']

def get_pets(owner_id):
    matching_pets = []
    for pet in pets:
        if pet['owner_id'] == owner_id:
            matching_pets.append(pet['name'])
    return matching_pets

pet_owner_id = get_owner_id(pet_owner_name)
pet_owner_pets = get_pets(pet_owner_id)

for pet in pet_owner_pets:
    print('-', pet)
