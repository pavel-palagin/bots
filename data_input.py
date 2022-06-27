import csv
from encodings import utf_8

def name_input():
    symbols = "!'@#$%^&*()`/:;.,?<>\|'""+-=[]}{"
    obj = input('Введите ФИО абонента: ')
    while True:
        for char in obj:
            if char.isdigit() or char in symbols:
                print('Вы ввели недопустимый символ, попробуйте снова')    
            else:
                return obj

def number_input():
    obj = input('Введите номер абонента в формате 8800123: ')
    while True: 
        for char in obj:
            if char.isdigit():
                return obj
            else:
                print('Вы ввели недопустимый символ, попробуйте снова ')    

def library_fill(card): #card - карточка абонента
        with open('library.csv', 'a', encoding='utf_8') as lib:
            csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
            writer = csv.writer(lib, 'my_dialect')
            writer.writerow(card)

def card_creator():
    card = input("Введите данные строго в формате -> Фамилия Имя Отчество Номер телефона Тип номера: ")
    card = card.split()
    return card

