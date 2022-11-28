
import inflect
from googletrans import Translator

def hello():
    print('Программа для работы с базой данных сотрудников')

def answer(data):
    print(data)


def button():
    inp = input('Для внесения данных нажмите "1"\nДля поиска данных нажмите "2"\nДля выхода нажмите "q"\nВведите символ:  ')
    return inp

def num_translate(data):                                        # Перевод чисел в слова
    translator = Translator()
    data = sum([list(i) for i in data], [])
    data = [str(item) for item in data]
    l2 = ''.join(data)
    p = inflect.engine()
    data = []
    for item in l2:
        if item.isdigit() == True:
            item = p.number_to_words(item)
            res = translator.translate(item, src='en', dest='ru') # Перевод чисел на русский язык
            data.append(res.text)
    print(data)
