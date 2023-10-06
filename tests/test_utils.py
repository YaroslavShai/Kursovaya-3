from utils import get_operations, filtered_data, get_last_data

def test_get_last_data(test_data):
    data = get_last_data(test_data)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']

def test_get_operations():
    data = get_operations()
    assert isinstance(data, list)

def test_filtered_data(test_data):
    data = filtered_data(test_data)
    assert len(data) == 4
