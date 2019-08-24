import csv
import json

csv_rows = []

with open('Fkko2019.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = dict(reader)
    print(data)

# with open('Fkko2019.json', 'w') as json_file:



# with open(json_path, 'w') as fh:
#        json.dump(data, fh, ensure_ascii=False)
