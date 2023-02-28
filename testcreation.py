import sqlite3

connection = sqlite3.connect('test.db') # connect to database

print(connection.total_changes) # will print 0 if no issues occur

cursor = connection.cursor() 

cursor.execute('CREATE TABLE animals (species TEXT, tier INTERGER, baseatk INTEGER, basehp INTEGER)') # start with basic categories

cursor.execute("INSERT INTO animals VALUES ('Otter', '1', '1', '2')")
cursor.execute("INSERT INTO animals VALUES ('Swan', '2', '1', '3')")
cursor.execute("INSERT INTO animals VALUES ('Badger', '3', '5', '3')")
cursor.execute("INSERT INTO animals VALUES ('Turtle', '4', '2', '5')")
cursor.execute("INSERT INTO animals VALUES ('Crocodile', '5', '8', '4')")
cursor.execute("INSERT INTO animals VALUES ('Gorilla', '6', '6', '9')")