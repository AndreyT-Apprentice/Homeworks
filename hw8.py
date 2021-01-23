#########################################################################################################
# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список (названия сохранить без точки).

import random


def read_data_from_domains():
    with open("./domains.txt", "r") as my_domains:
        domains_list = [line.rstrip()[1:] for line in my_domains]
        return domains_list


#########################################################################################################
# 2. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

def read_data_from_names():
    with open("./names.txt", "r") as my_names:
        names_list = [line.rstrip().split()[1].lower() for line in my_names]
        return names_list


#########################################################################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
#
# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com

def create_random_number():
    random_number = random.randint(100, 999)
    return random_number


def create_random_string(min_len=5, max_len=7):
    random_string = ("".join(random.choice(chr(random.randint(ord('a'), ord('z'))))
                             for _ in range(random.randint(min_len, max_len))))
    return random_string


def create_email(names_list, domains_list):
    name = random.choice(names_list)
    domain = random.choice(domains_list)
    number = create_random_number()
    string = create_random_string()
    new_email = f"{name}.{number}@{string}.{domain}"
    return new_email


names = read_data_from_names()
domains = read_data_from_domains()
e_mail = create_email(names, domains)
print(e_mail)