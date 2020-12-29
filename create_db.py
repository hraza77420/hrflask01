__author__ = 'miranaraza'
import sqlite3

con = sqlite3.connect("student.db")
print("Opened database successfully")

con.execute("CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")

con.close()
