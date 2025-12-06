import json

people_string = '''
{
  "people": [
    {
      "name": "Virat",
      "phone": "6767393890",
      "emails": ["virat4@gmail.com", "virat01@infosys.com"],
      "has_license": false
    },
    {
      "name": "Deva",
      "phone": "3544887",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data))

print(type(data['people']))

for person in data['people']:
    print(person)

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2,sort_keys=True)
print(new_string)






















