from utils import get_operations, filtered_data, get_last_data


def main():
    data = get_operations()
    data = filtered_data(data)
    data = get_last_data(data)
    for i in data:
        date = i['date'].replace('-', '.')[0:10]
        correct_date = f'{date[5:7]}.{date[8:10]}.{date[:4]}'

        operationAmount = (i['operationAmount'])
        currency = (operationAmount['currency'])
        to = i['to']
        if 'Счет' in i['to']:
            t = f"Счёт **{(i['to'])[-5:-1]}"

        if i['description'] == 'Открытие вклада':
            print(f"""{correct_date} {i['description']}
->  {t}
{operationAmount['amount']} {currency['name']}\n""")

        else:
            f = i['from']
            if 'Visa Classic' in f:
                f = f"{f[:12]} {f[13:17]} {f[17:19]}** **** {f[25:30]}"

            elif 'Maestro' in f:
                f = f"{f[:7]} {f[8:12]} {f[12:14]}** **** {f[19:]}"

            elif 'Счет' in f:
                f = f"Счёт **{(i['to'])[-5:-1]}"


            print(f"""{correct_date} {i['description']}
{f} -> {t}
{operationAmount['amount']} {currency['name']}\n""")






if __name__ == "__main__":
    main()

