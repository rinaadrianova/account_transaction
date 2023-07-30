from src.utils import transfer_date, transaction_cards, get_last_five


def test_transfer_date():
    assert transfer_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert transfer_date("2018-06-30T02:08:58.425572") == "30.06.2018"
    assert transfer_date("2018-03-23T10:45:06.972075") == "23.03.2018"
    assert transfer_date("2018-03-23T") == "23.03.2018"


def test_transaction_cards():
    assert transaction_cards() == 'Не указано'
    assert transaction_cards('') == 'Не указано'
    assert transaction_cards("Счет 75106830613657916952") == 'Счет **6952'
    assert transaction_cards("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'


def test_last_five():
    test_data = [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  },
  {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  },
  {
    "id": 522357576,
    "state": "EXECUTED",
    "date": "2019-07-12T20:41:47.882230",
    "operationAmount": {
      "amount": "51463.70",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 48894435694657014368",
    "to": "Счет 38976430693692818358"
  }]
    assert len(get_last_five(test_data)) == 5



