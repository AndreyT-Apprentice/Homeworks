#########################################################################################################
# 1. Дано целое число (int). Определить сколько нулей в этом числе.

my_int = int(1000000000)
my_str = str(my_int)
my_symbol = "0"
count = my_str.count(my_symbol)
print(count)


#########################################################################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

my_int = int(1000010000)
count = 0
while my_int % 10 == 0:
    my_int //= 10
    count += 1
print(count)


#########################################################################################################
# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
my_result = list(my_list_1[::2])+(my_list_2[1::2])
print(my_result)


#########################################################################################################
# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]

my_list_1 = [1, 2, 3, 4, 5, 6, 7]
my_list_2 = [10, 15, 20, 25, 33]
my_result = []
for element in my_list_1:
    if element % 2 == 0:
        my_result.append(element)
for element in my_list_2:
    if element % 2 != 0:
        my_result.append(element)
print(my_result)


#########################################################################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list_1 = [1, 2, 3, 4, 5, 6, 7]
new_list = list((my_list_1[1:])+(my_list_1[0:1]))
print(new_list)


#########################################################################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list_1 = [1, 2, 3, 4, 5, 6, 7]
my_list_1.append(my_list_1.pop(0))
print(my_list_1)


#########################################################################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

my_str = str("43 больше чем 34 но меньше чем 56")
my_list = list(my_str.split(' '))
my_sum_list = []
for index in my_list:
    if index.isnumeric():
        my_sum_list.append(index)
my_sum = sum(map(int, my_sum_list))
print(my_sum)


#########################################################################################################
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = str("asdfasa")
n = 2
if len(my_str) % 2 != 0:
    my_str = my_str + '_'
my_list = list(my_str[index:index+2] for index in range(0, len(my_str), n))
print(my_list)


#########################################################################################################
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

# Вариант 1
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
sub_str = my_str.split(l_limit)[1].split(r_limit)[0]
print(sub_str)

# Вариант 2
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
l_limit_first = my_str.index(l_limit) + len(r_limit)
r_limit_first = my_str.index(r_limit, l_limit_first)
sub_str = my_str[l_limit_first:r_limit_first]
print(sub_str)


#########################################################################################################
# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

# Вариант 1
my_str = "My long string"
l_limit = "o"
r_limit = "g"
l_limit_first = my_str.index(l_limit) + len(l_limit)
r_limit_first = my_str.index(r_limit) + len(r_limit)
r_limit_second = my_str.index(r_limit, r_limit_first + 1)
sub_str = my_str[l_limit_first:r_limit_second]
print(sub_str)

# Вариант 2
my_str = "oMMMoMMMMy long stringwwwwwwg"
l_limit = "o"
r_limit = "g"
list_limit_l = []
list_limit_r = []
for index, word in enumerate(my_str):
    if word == l_limit:
        list_limit_l.append(index)
    elif word == r_limit:
        list_limit_r.append(index)
min_l = min(list_limit_l)
max_r = max(list_limit_r)
sub_str = my_str[min_l + 1:max_r]
print(sub_str)


#########################################################################################################
# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
len_my_list = len(my_list)
count = 0
sum_result = []
for index in range(len(my_list))[1:-1]:
    sum_result = my_list[index - 1] + my_list[(index + 1) % len_my_list]
    if my_list[index] > sum_result:
        count += 1
print(count)