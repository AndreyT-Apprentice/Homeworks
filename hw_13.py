# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroPython_18_11/blob/main/Homeworks/lesson8.txt
#
# Суть задания - сздать класс EmailGenerator
#
# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")
#
# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names(). (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = self.get_domains()
# self.names = self.get_names()
#
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
#
# 4. Написать метод экземпляра класса generate_email() (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com

import random


class EmailGenerator:
    def __init__(self, domains_path="./domains.txt", names_path="./names.txt"):
        self.domains_path = domains_path
        self.names_path = names_path
        self.domains = self.read_data_from_domains()
        self.names = self.read_data_from_names()
        self.create_random_number()
        self.create_random_string()

    def __repr__(self):
        return f"Len Domains: {len(self.domains)}, Len Names: {len(self.names)}"

    def read_data_from_domains(self):
        with open("domains.txt", "r") as self.domains:
            domains_list = [line.rstrip()[1:] for line in self.domains]
            return domains_list

    def read_data_from_names(self):
        with open("./names.txt", "r") as self.names:
            names_list = [line.rstrip().split()[1].lower() for line in self.names]
            return names_list

    def create_random_number(self):
        random_number = random.randint(100, 999)
        return random_number

    def create_random_string(self, min_len=5, max_len=7):
        random_string = ("".join(random.choice(chr(random.randint(ord('a'), ord('z'))))
                                 for _ in range(random.randint(min_len, max_len))))
        return random_string

    def create_email(self):
        name = random.choice(self.names)
        domain = random.choice(self.domains)
        number = self.create_random_number()
        string = self.create_random_string()
        new_email = f"{name}.{number}@{string}.{domain}"
        return new_email


email_generator = EmailGenerator("domains.txt", "names.txt")
print(email_generator)
email = email_generator.create_email()
print(email)