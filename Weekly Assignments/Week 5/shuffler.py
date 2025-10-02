import json
import random

with open('registrations.old.json') as f:
    registrations = json.load(f)

random.shuffle(registrations)

with open('registrations.json', 'w') as f:
    json.dump(registrations, f, indent=2)
