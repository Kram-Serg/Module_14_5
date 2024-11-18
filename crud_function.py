import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()


def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False


def add_product():

    producte1 = ['SLIM FORMULA', 'Ускоряет расщепление жира,снижает аппетит', 1200]
    producte2 = ['OMEGA-3 75%', 'Биологически активная добавка к пище "Омеrа-3 75%"', 1600]
    producte3 = ['Detox', 'Комплекс для очищения печени', 2200]
    producte4 = ['MAGNESIUM SALT EPSON', 'Английская магниевая соль для принятия ванны', 800]

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte1)
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte2)
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte3)
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte4)

    connection.commit()


def get_all_products():
    product = cursor.execute('SELECT title, description, price FROM Products').fetchall()
    connection.commit()
    return product


initiate_db()
# add_product()
# add_user('Sergei', 'exempl1@gmail.com', 35)
# add_user('Olesya', 'exempl2@gmail.com', 32)
# add_user('Ilya', 'exempl3@gmail.com', 22)
# add_user('Galina', 'exempl4@gmail.com', 58)
