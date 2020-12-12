#########################################################################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ['qwe', 'rty', 'uio', 'asd', 'fgh']
result_list = []
for index, word in enumerate(my_list):
    if index % 2 != 0:
        result_list.append(word[::-1])
    else:
        result_list.append(word)
print(result_list)


#########################################################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['qwe', 'rty', 'uio', 'asd', 'fgh', 'azx', 'qwa']
result_list = []
for word in my_list:
    if word[0] == 'a':
        result_list.append(word)
print(result_list)


#########################################################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['qwe', 'rty', 'uio', 'asd', 'fgh', 'azx', 'qwa']
result_list = []
for word in my_list:
    if 'a' in word:
        result_list.append(word)
print(result_list)


#########################################################################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['qwe', 1, 'rty', 2, 'uio', 3, 'asd', 4, 'fgh', 5, 'azx', 6, 'qwa']
result_list = []
for element in my_list:
    if element == str(element):
        result_list.append(element)
print(result_list)


#########################################################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = str('adsfadfadfaq')
result_list = []
for index in my_str:
    if my_str.count(index) == 1:
        result_list.append(index)
print(result_list)


#########################################################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = str('qfgshghg')
my_str_2 = str('qwgerty')
my_set = set(my_str_1)
result_list = list(my_set.intersection(my_str_2))
print(result_list)


#########################################################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = str('qweax')
my_str_2 = str('asdqax')
my_list_1 = []
my_list_2 = []
for index in my_str_1:
    if my_str_1.count(index) == 1:
        my_list_1.append(index)
for index in my_str_2:
    if my_str_2.count(index) == 1:
        my_list_2.append(index)
set_result_list_1 = set(my_list_1)
result_list = list(set_result_list_1.intersection(my_list_2))
print(result_list)


#########################################################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

person = {
    'Second name': "da Vinci",
    'First name': 'Leonardo',
    'Age': 67,
    'Location': {
        'Country': 'Republic of Florence',
        'City': 'Vinci',
        'Street': 'Leonardo street'
    },
    'Job': {
        'Employment': '+',
        'Position': 'Polymath'
    }}
print(person)


#########################################################################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

Components = {
    'Cake': {
        'Flour': '300 grams',
        'Milk': '250 milliliters',
        'Butter': '50 grams',
        'Eggs': 'two'
    },
    'Cream': {
        'Sugar': '50 grams',
        'Butter': '100 grams',
        'Vanilla': '10 grams',
        'Sour cream': '20 grams'
    },
    'Glaze': {
        'Cocoa': '30 grams',
        'Sugar': '50 grams',
        'Butter': '10 grams'
    }}
print(Components)