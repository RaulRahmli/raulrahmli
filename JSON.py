import json

with open('Raul.json', 'r') as file:
    json_str = file.read()

# parse x:
y = json.loads(json_str)

# the result is a Python dictionary:
print(y["age"])