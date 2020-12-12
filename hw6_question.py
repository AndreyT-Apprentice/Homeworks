#########################################################################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['qwe', 1, 'rty', 2, 'uio', 3, '3', 'asd', 4, 'fgh', 5, 'azx', 6, 'qwa']
result_list = []
for element in my_list:
    if element == str(element):
        result_list.append(element)
print(result_list)


my_list = ['qwe', 1, 'rty', 2, 'uio', 3, '3', 'asd', 4, 'fgh', 5, 'azx', 6, 'qwa']
result_list = []
for element in my_list:
    if type(element) == str:
        result_list.append(element)
print(result_list)