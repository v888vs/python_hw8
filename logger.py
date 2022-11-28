from datetime import datetime as dt


def log_info(action):
    act1 = ''
    if action == '1':
        act1 = 'record'
    elif action == '2':
        act1 = 'read'
    time = dt.now().strftime('%H:%M:%S')
    with open('log.txt', 'a', encoding='utf-8') as rec:
        rec.write(f'{act1} {time} \n')