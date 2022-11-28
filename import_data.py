import csv
import os.path
import view

def find_surname(surname):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if surname == item[0]:
                    view.answer(item)
                    view.num_translate(item)
                    count+=1
            if count == 0:
                view.answer(f'{surname} не найден!')
    else:
        view.answer('Файл не найден!')


def find_name(name):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if name == item[1]:
                    view.answer(item)
                    view.num_translate(item)
                    count+=1
            if count == 0:
                view.answer(f'{name} не найден!')
    else:
        view.answer('Файл не найден!')


def find_ph_num(ph_num):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if ph_num == item[2]:
                    view.answer(item)
                    view.num_translate(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с телефоном {ph_num} не найден!')
    else:
        view.answer('Файл не найден!')

def find_occupation(occup):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if occup == item[3]:
                    view.answer(item)
                    view.num_translate(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с должностью {occup} не найден!')
    else:
        view.answer('Файл не найден!')