import json
import requests

data = {'name': 'Someone', 'age': 30, 'school': 'Somewhere'}

print(requests.get('https://google.com').status_code)

#print(data, type(data))

# Convert dictionary to a Python JSON
"""data = json.dumps(data)
print(data, type(data))

# Convert Json to dictionnary
data = json.loads(data)
17 18 19 20 21 22 23 24 01 02 03 04 05 06 07
print(data, type(data))"""