from utils import get_operations, filtered_data, get_last_data


def main():
    data = get_operations()
    data = filtered_data(data)
    data = get_last_data(data)
    for i in data:
        operationAmount = (i['operationAmount'])
        currency = (operationAmount['currency'])

        if i['description'] == 'Открытие вклада':
            print(f"""{(i['date'])[0:10]} {i['description']}
->  Счёт **{(i['to'])[-5:-1]}
{operationAmount['amount']} {currency['code']}\n""")

        elif i['description'] == 'Перевод организации':
            print(f"""{(i['date'])[0:10]} {i['description']}
{i['from']} -> {i['to']}
{operationAmount['amount']} {currency['code']}\n""")

        elif i['description'] == 'Перевод со счета на счет':
            print(f"""{(i['date'])[0:10]} {i['description']}
{i['from']} -> {i['to']}
{operationAmount['amount']} {currency['code']}\n""")

        elif i['description'] == 'Перевод с карты на карту':
            print(f"""{(i['date'])[0:10]} {i['description']}
{i['from']} -> {i['to']}
{operationAmount['amount']} {currency['code']}\n""")

        elif i['description'] == 'Перевод с карты на счет':
            print(f"""{(i['date'])[0:10]} {i['description']}
{i['from']} -> {i['to']}
{operationAmount['amount']} {currency['code']}\n""")

        elif i['description'] == 'Перевод со счета на карту':
            print(f"""{(i['date'])[0:10]} {i['description']}
{i['from']} -> {i['to']}
{operationAmount['amount']} {currency['code']}\n""")




if __name__ == "__main__":
    main()
