import csv
import json

list_common = [[[], [], []], [[], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], [], [], []]]

with open('Fkko2019.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if row[0][0] == '1':
            if row[0][2] == '0':
                list_common[0].append(row)
            elif row[0][2] == '1':
                list_common[0][0].append(row)
            elif row[0][2] == '5':
                list_common[0][1].append(row)
            elif row[0][2] == '7':
                list_common[0][2].append(row)

        elif row[0][0] == '2':
            if (row[0][2] == '0') and (row[0][5] == '0'):
                list_common[1].append(row)
            elif row[0][2] == '0':
                list_common[1][0].append(row)
            elif row[0][2] == '1':
                list_common[1][1].append(row)
            elif row[0][2] == '2':
                list_common[1][2].append(row)
            elif row[0][2] == '3':
                list_common[1][3].append(row)
            elif row[0][2] == '8':
                list_common[1][4].append(row)
            elif row[0][2] == '9':
                list_common[1][5].append(row)

        elif row[0][0] == '3':
            if (row[0][2] == '0') and (row[0][3] == '0'):
                list_common[2].append(row)
            elif row[0][2] == '0':
                list_common[2][0].append(row)
            elif row[0][2] == '1':
                list_common[2][1].append(row)
            elif row[0][2] == '3':
                list_common[2][2].append(row)
            elif row[0][2] == '4':
                list_common[2][3].append(row)
            elif row[0][2] == '5':
                list_common[2][4].append(row)
            elif row[0][2] == '6':
                list_common[2][5].append(row)
            elif row[0][2] == '7':
                list_common[2][6].append(row)
            elif row[0][2] == '8':
                list_common[2][7].append(row)
            elif row[0][2] == '9':
                list_common[2][8].append(row)

        elif row[0][0] == '4':
            if (row[0][2] == '0') and (row[0][3] == '0'):
                list_common[3].append(row)
            elif row[0][2] == '0':
                list_common[3][0].append(row)
            elif row[0][2] == '1':
                list_common[3][1].append(row)
            elif row[0][2] == '3':
                list_common[3][2].append(row)
            elif row[0][2] == '4':
                list_common[3][3].append(row)
            elif row[0][2] == '5':
                list_common[3][4].append(row)
            elif row[0][2] == '6':
                list_common[3][5].append(row)
            elif row[0][2] == '7':
                list_common[3][6].append(row)
            elif row[0][2] == '8':
                list_common[3][7].append(row)
            elif row[0][2] == '9':
                list_common[3][8].append(row)

        elif row[0][0] == '6':
            if row[0][2] == '0':
                list_common[4].append(row)
            elif row[0][2] == '1':
                list_common[4][0].append(row)
            elif row[0][2] == '2':
                list_common[4][1].append(row)
            elif row[0][2] == '3':
                list_common[4][2].append(row)
            elif row[0][2] == '4':
                list_common[4][3].append(row)
            elif row[0][2] == '9':
                list_common[4][4].append(row)

        elif row[0][0] == '7':
            if row[0][2] == '0':
                list_common[5].append(row)
            elif row[0][2] == '1':
                list_common[5][0].append(row)
            elif row[0][2] == '2':
                list_common[5][1].append(row)
            elif row[0][2] == '3':
                list_common[5][2].append(row)
            elif row[0][2] == '4':
                list_common[5][3].append(row)
            elif row[0][2] == '6':
                list_common[5][4].append(row)

        elif row[0][0] == '8':
            if row[0][2] == '0':
                list_common[6].append(row)
            elif row[0][2] == '1':
                list_common[6][0].append(row)
            elif row[0][2] == '2':
                list_common[6][1].append(row)
            elif row[0][2] == '3':
                list_common[6][2].append(row)
            elif row[0][2] == '4':
                list_common[6][3].append(row)
            elif row[0][2] == '8':
                list_common[6][4].append(row)
            elif row[0][2] == '9':
                list_common[6][5].append(row)

        elif row[0][0] == '9':
            if row[0][2] == '0':
                list_common[7].append(row)
            elif row[0][2] == '1':
                list_common[7][0].append(row)
            elif row[0][2] == '2':
                list_common[7][1].append(row)
            elif row[0][2] == '3':
                list_common[7][2].append(row)
            elif row[0][2] == '4':
                list_common[7][3].append(row)
            elif row[0][2] == '5':
                list_common[7][4].append(row)
            elif row[0][2] == '6':
                list_common[7][5].append(row)

print(list_common)
with open('test2.json', 'w') as fh:
    json.dump(list_common, fh, ensure_ascii=False)

