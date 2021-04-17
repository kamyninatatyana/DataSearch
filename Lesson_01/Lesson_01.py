import requests
import json

# Задание 1
# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

print('Задание 1')
print()

user_name = 'kamyninatatyana'
my_url = 'https://api.github.com'
my_request = requests.get(f'{my_url}/users/{user_name}/repos')

print(f'Список репозиториев пользователя {user_name}')

with open('task_1.json', 'w') as my_file:
    json.dump(my_request.json(), my_file)

counter = 1
for item in my_request.json():
    print(counter, item["name"])
    counter = counter + 1


# Задание 2
# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

print()
print('Задание 2')

my_url = 'https://api.nasa.gov/'
api_key = 'Rfnkizox7W8yF2PXVgFxfa4AcmQJqknrkK9h8r2P'
params = {'api_key': api_key}
my_link = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json'
my_request = requests.get('https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json', params=params)

with open('task_2.json', 'w') as my_file:
    json.dump(my_request.json(), my_file)

print(f'Названия планет')

counter = 1
for item in my_request.json():
    while counter < 100:
        print(counter, item['pl_name'])
        counter = counter + 1