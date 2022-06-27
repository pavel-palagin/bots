import data_input
import csv
from encodings import utf_8
find_type = ''

def searching_sabscribers():
    result = ''
    with open('library.csv', encoding='utf_8') as lib:
        read_data = csv.reader(lib, delimiter="|")
        for line in read_data:
            if line == []:
                continue
            if find_type == 'Найти по ФИО':
                name = data_input.name_input().split()
                if name in (line[0:3], line[0:2], line[0:1], line[1:2]) :
                    result += str(line[0:]) + '\n'
            if find_type == 'Найти по номеру':
                number = data_input.number_input().split()
                if line[3] == number[0]:
                    result += str(line[0:]) + '\n'
    return result





# def search_for_name():
#     result = ''
#     with open('library.csv', encoding='utf_8') as lib:
#         read_data = csv.reader(lib, delimiter="|")
#         name = data_input.name_input().split()
#         for line in read_data:
#             if name in (line[0:3], line[0:2], line[0:1], line[1:2], line[2:3]):
#                 result += str(line[0:]) + '\n'
#     return result
#
# def search_for_number():
#     result = ''
#     with open('library.csv', encoding='utf_8') as lib:
#         read_data = csv.reader(lib, delimiter="|")
#         number = data_input.number_input().split()
#         for line in read_data:
#             if line == []:
#                 continue
#             if line[3] == number[0]:
#                 result += str(line[0:]) + '\n'
#         return result




