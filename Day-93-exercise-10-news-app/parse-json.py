import json

response_string = """
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 30,
  "isEmployee": true,
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  },
  "phoneNumbers": [
    "555-1234",
    "555-5678"
  ]
}
"""

data = json.loads(response_string)

print(f"Name: {data['firstName']} {data['lastName']}")
print(f"Age: {data['age']}")
print(f"Employee: {'Yes' if data['isEmployee'] else 'No'}")
print(f"City: {data['address']['city']}")
print(f"Street: {data['address']['street']}")
print("Phones: ")
for phone in data['phoneNumbers']:
  print(f"* {phone}")