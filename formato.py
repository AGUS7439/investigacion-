import csv
import json

with open('datos.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open('datos.json', mode='w') as json_file:
    json.dump(data, json_file, indent=4)
