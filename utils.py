import json


def get_last_data(data):
    data = sorted(data, key=lambda x:x["date"], reverse=True)

    return data[:5]

def filtered_data(data):
    new_data = []
    for i in data:
        if i and i["state"] == "EXECUTED":
            new_data.append(i)

    return new_data


def get_operations():
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)
