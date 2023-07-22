import json
from datetime import datetime

with open('operations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def executed_transaction():
    count = 0
    last_five = []
    while count < 5:
        if data[count].get('state') == "EXECUTED":
            last_five.append(data[count])
            count += 1
    return last_five


def transfer_date(date):
    '''
    Обрабатывает и возвращает дату в формате
    дд.мм.гггг
    '''

    date_num = date.split('T')[0]
    dateobj = datetime.strptime(date_num, '%Y-%m-%d')
    formatted_date = dateobj.strftime('%d.%m.%Y')
    return formatted_date

def transaction_cards(card_number):
    '''
    Принимает имя и номер карты или счета и возвращает
    в отформатированном виде
    :param card_number:
    '''
    if 'Счет' not in card_number:
        card_num = card_number[-16:]
        card_name = card_number[:-16].rstrip()
        return f'{card_name} {card_num[:4]} {card_num[4:6]}** **** {card_number[-4:]}'
    else:
        card_num = card_number[-20:]
        card_name = card_number[:-20].rstrip()
        return f'{card_name} **{card_num[-4:]}'

