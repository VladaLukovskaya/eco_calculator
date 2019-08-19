dict = {}

def find_all(string):
    while len(string) > 0:
        dict = find_code(string)
        string = string[index:]
    return dict

def find_code(string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    code = list()
    name = ''
    for elem in range(len(string)):
        if string[elem] in numbers:
            code.append(string[elem])
        elif ord(string[elem]) == 32:
            continue
        else:
            string = string[elem:]
            for symbol in range(len(string)):
                if string[symbol] not in numbers:
                    name += string[symbol]
                    if symbol == (len(string) - 1):
                        dict[str(code)] = name
                        return dict
                    # если это последний элемент, он должен записываться в словарь, затем выход из цикла
                else:
                    dict[str(code)] = name
                    global index
                    index = elem + len(name)
                    return dict


find_all('221 711 31 394осадок мокрой газоочистки при обогащении железных руд221 811 И 395отходы (осадок) механической очистки шахтно-рудничных вод при добыче железных руд2 21 821 11 39 5отходы (осадок) механической очистки сто')
