dict = {}


def edit_code(code):
    if len(code) == 11:
        new_code = code[:]
        code = [' ' for i in range(16)]
        code[0] = new_code[0]
        code[2] = new_code[1]
        code[3] = new_code[2]
        code[5] = new_code[3]
        code[6] = new_code[4]
        code[7] = new_code[5]
        code[9] = new_code[6]
        code[10] = new_code[7]
        code[12] = new_code[8]
        code[13] = new_code[9]
        code[15] = new_code[10]
        code = ''.join(code)
    else:
        code = str(code)
    return code


def find_all(string):
    all = list()
    while len(string) > 0:
        nested_list = find_code(string)
        all.append(nested_list)
        string = string[index:]
    return all

def find_code(string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    nested_list = ['', '']
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
                        first_elem = edit_code(code)
                        sec_elem = name
                        nested_list[0] = first_elem
                        nested_list[1] = sec_elem
                        return nested_list
                    # если это последний элемент, он должен записываться в словарь, затем выход из цикла
                else:
                    first_elem = edit_code(code)
                    sec_elem = name
                    nested_list[0] = first_elem
                    nested_list[1] = sec_elem
                    global index
                    index = elem + len(name)
                    return nested_list


find_all('221 711 31 394осадок мокрой газоочистки при обогащении железных руд221 811 И 395отходы (осадок) механической очистки шахтно-рудничных вод при добыче железных руд2 21 821 11 39 5отходы (осадок) механической очистки сто')

# bar = ['2', '2', '1', '7', '1', '1', '3', '1', '3', '9', '4']
# edit_code(bar)
