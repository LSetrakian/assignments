# KATIE S and LISA S

# Read Superheroes.json 
import json
from pprint import pprint

with open('superheroes.json', 'r') as f:
    squad = json.load(f)
    
# Create empty array called powers
allpowers = []

# Loop through members of squad
members = squad['members']
for member in members:
	# and append the power of each to the power array
	powers = member['powers']
	for power in powers:
		allpowers.append(power)

# Print each power to terminal
pprint(allpowers)