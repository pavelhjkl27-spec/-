from csv import reader
import xml.dom.minidom as minidom

# Задание №1.
print('Задание №1')
print()
with open('books.csv', 'r') as csvfile:
    file_reader = list(reader(csvfile, delimiter=';'))
    count = 0
    for i in file_reader[1:]:
        if len(i[1]) > 30:
            count += 1
    print(f'Количество записей, у которых в поле \'Название\'\n'
          f'строка длиннее 30-и символов: {count}')

print()

# Задание №2.
print('Задание №2')
print()
with open('books.csv', 'r') as csvfile:
    file_reader = list(reader(csvfile, delimiter=';'))
    search_data = input('Введите ФИО автора книги: ')
    books = []
    flag = True

    for i in file_reader:
        if i[4] == search_data:
            flag = False
            if int(i[6][6:10]) >= 2018:
                books.append(f'Название книги с {int(i[6][6:10])}-го года: {i[1]}')

    if flag:
        print('Такого автора не найдено!')
    else:
        if books:
            print('\n'.join(books))
        else:
            print('Книги с 2018-го года от этого автора не найдено!')

print()

# Задание №3.
print('Задание №3')
print()
file = open('file.txt', 'w')
with open('books.csv', 'r') as csvfile:
    file_reader = list(reader(csvfile, delimiter=';'))
    count = 0
    for i, j in enumerate(file_reader):
        if i % 2 == 0 and i != 0:
            file.write(f'{count + 1}) {j[3]}. {j[1]} - {j[6][6:10]}-й год.\n')
            count += 1
        if count == 20:
            break
file.close()

print()

# Задание №4.

print('Задание №4')
print()

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

dct = {}

valute = dom.getElementsByTagName('Valute')
for i in valute:
    name = i.getElementsByTagName('Name')[0].firstChild.data
    CharCode = i.getElementsByTagName('CharCode')[0].firstChild.data
    dct[name] = CharCode
for i in dct:
    print(f'{i}: {dct[i]}')