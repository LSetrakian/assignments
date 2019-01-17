# Read superheroes.json
import json
import csv
from pprint import pprint

with open('superheroes.json', 'r') as f:
	reader = json.load(f)
	
with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	# Write a header to CSV file
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])


	# Loop over members and write one row per member
	members = reader['members']
	for member in members:
		name = member['name']
		age = member['age']
		secretIdentity = member['secretIdentity']
		powers = member['powers']
		squadName = 'squadName'
		homeTown = 'homeTown'
		formed = 'formed'
		secretBase = 'secretBase'
		active = 'active'
		writer.writerow([name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active])

pprint(members)