def edit_code(code):  # если полученный код правильный, приводим его к нужному виду, иначе оставляем
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
        code = str(code)  # в таком виде неправильный код будет сразу заметен в документе
    return code


def find_all(string):  # функция поиска всех пар "код-наименование"
    all = list()
    while len(string) > 0:  # после получения новой пары мы добавляем её в список, удаляем из строки и проходимся снова
        nested_list = find_code(string)
        all.append(nested_list)
        string = string[index:]
    return all

def find_code(string):  # ищем одну пару "код-наименование"
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    nested_list = ['', '']
    code = list()
    name = ''
    for elem in range(len(string)):  # все цифры из строки записываем в код, а все буквы - в наименование, \
        # затем помещаем эту пару в список
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
                else:
                    first_elem = edit_code(code)
                    sec_elem = name
                    nested_list[0] = first_elem
                    nested_list[1] = sec_elem
                    global index
                    index = elem + len(name)  # последний элемент + длина наименования в сумме дают индекс того \
                    # элемента, на котором остановились и с которого надо начать следующий проход по циклу
                    return nested_list

find_all('7 39 400 00 00 0Отходы при предоставлении услуг парикмахерскими, салонамикрасоты, соляриями, банями, саунами, \
относящиеся к  твердымкоммунальным отходам7 39 410 00 00 0Отходы (мусор) от уборки парикмахерских,  салонов красоты,  \
соляриев7 39 410 01 72 4отходы (мусор) от уборки помещений парикмахерских, салонов красоты, соляриев7 39 411 31 72 4отходы\
 ватных дисков, палочек, салфеток с остатками косметических средств7 39413  11 29 5отходы волос7 39 420 00 00 0Отходы  \
 (мусор) от уборки бань,  саун,  прачечных')
