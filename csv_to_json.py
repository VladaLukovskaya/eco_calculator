import csv
import json

template = '{{"": "{}", "": "{}", "": {{"": {}, "": {}}}}}'
result = []
with open('Fkko2019.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        result.append(list)
print(result)

# print(*([json.dumps(j, sort_keys=True,
 #                   ensure_ascii=False,
  #                  indent=4) for j in result]), sep=',\n')
