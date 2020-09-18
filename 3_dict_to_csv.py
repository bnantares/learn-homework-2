"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    some_list = [
            {'name': 'Maria', 'age': 25, 'job': 'Scientist'}, 
            {'name': 'Vasia', 'age': 8, 'job': 'Programmer'}, 
            {'name': 'Eduardo', 'age': 48, 'job': 'Big boss'},
            {'name': 'Vladimir', 'age': 27, 'job': 'Bruh'},
            {'name': 'Ann', 'age': 22, 'job': 'Writer'}
        ]    

    with open('people.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in some_list:
            writer.writerow(user)


if __name__ == "__main__":
    main()
