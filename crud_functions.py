import sqlite3
import random
from distutils.command.check import check

#Создайте файл crud_functions.py и напишите там следующие функции:

# connection = sqlite3.connect('products.db')
# cursor = connection.cursor()

#initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
    # id - целое число, первичный ключ
    # title(название продукта) - текст (не пустой)
    # description(описание) - текст
    # price(цена) - целое число (не пустой)

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

# get_all_products, которая возвращает все записи из таблицы Products,
# полученные при помощи SQL запроса.

def get_all_products():
    initiate_db()
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products

# заполнили таблицу
# for _ in range(4):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#                     (f'Продукт {_ + 1}', f'Описание {_ + 1}', f'{(_ + 1) * 100}'))

# connection.commit()
# connection.close()