#########################################################################################################
# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random

# var 1
result_list = []
for number in range(20):
    number = random.randint(1, 100)
    result_list.append(number)
print(result_list)

# var 2
list_res = list([random.randint(1, 100) for number in range(20)])
print(list_res)


#########################################################################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10
# по каждой оси.

triangle = {'A': (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            'B': (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10)),
            'C': (random.randint(-10, 10),
                  random.randint(-10, 10),
                  random.randint(-10, 10))
            }
print(triangle)


#########################################################################################################
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "I'm the string"


def my_print():
    my_string = (3 * '*') + my_str + (3 * '*')
    return print(my_string)


my_print()


#########################################################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "Fill", "age": 12},
           {"name": "Johnny", "age": 15},
           {"name": "Nick", "age": 12},
           {"name": "Jack", "age": 45}]

# a)
my_age = []
for value_1 in persons:
    age = value_1["age"]
    my_age.append(age)
min_age_val = min(my_age)
for value_2 in persons:
    if value_2["age"] == min_age_val:
        print(value_2["name"])

# б)
max_len = max(len(value["name"]) for value in persons)
for value in persons:
    if len(value["name"]) == max_len:
        print(value["name"])

# в)
age_sum = 0
count_values = []
count_values_int = 0
for value in persons:
    age_sum += value["age"]
    count_values.append(value)
    count_values_int += count_values.count(value)
result = age_sum / count_values_int
print(result)


#########################################################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {"name": "Fill", "age": 12, "weight": 60, "blood type": "A+"}
my_dict_2 = {"name": "Johnny", "age": 15, "height": 1.70, "foot size": 39, "blood type": "A-"}

# а)
my_set_1 = set(my_dict_1)
my_list = list(my_set_1.intersection(my_dict_2))
print(my_list)

# б)
my_set_1 = set(my_dict_1)
my_list = list(my_set_1.difference(my_dict_2))
print(my_list)

# в)
new_dict = {}
for key in my_dict_1:
    if key not in my_dict_2:
        new_dict[key] = my_dict_1[key]
print(new_dict)

# г)
new_dict = {}
for key in my_dict_1:
    if key not in my_dict_2:
        new_dict[key] = my_dict_1[key]
for key in my_dict_2:
    if key not in my_dict_1:
        new_dict[key] = my_dict_2[key]
    else:
        new_dict[key] = my_dict_1[key], my_dict_2[key]
print(new_dict)