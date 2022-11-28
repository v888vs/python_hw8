import export_data as exp
import import_data as imp
import view


import logger as log

def button_click():
    view.hello()
    choise = view.button()
    while choise != 'q':
        log.log_info(choise)
        if choise == '1':
            exp.export_data()
        elif choise == '2':
            what_find = input('Для поиска по фамилии введите "1"\nДля поиска по имени введите "2"\nДля поиска введите номер"3"\nДля поиска введите должнотсь"4"\nВведите символ:  ')
            if what_find == '1': imp.find_surname(input('Введите фамилию: '))
            if what_find == '2': imp.find_name(input('Введите имя: '))
            if what_find == '3': imp.find_ph_num(input('Введите телефон: '))
            if what_find == '4': imp.find_occupation(input('Введите должнотсь: '))
        choise = view.button()

