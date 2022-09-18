import sqlite3

def conectar():
    database= sqlite3.connect('pizzeria.db')
    print(database)
    cursor=database.cursor()