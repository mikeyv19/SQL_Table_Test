# Import required modules
import csv
import sqlite3

# Connecting to the geeks database
connection = sqlite3.connect("food.db")

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
# create_table = '''CREATE TABLE person(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 age INTEGER NOT NULL);
#                 '''

# Creating the table into our
# database
# cursor.execute(create_table)

# Opening the person-records.csv file
file = open("unit.csv")

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# SQL query to insert data into the
# unit table
insert_records = "INSERT INTO unit (id, oid, name) VALUES(?, ?, ?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM unit"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# IMPORT AISLE
file = open("aisle.csv")


contents = csv.reader(file)

insert_records = "INSERT INTO aisle (id, name) VALUES(?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM aisle"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)
connection.commit()

# Import ingredient
file = open("ingredient.csv")


contents = csv.reader(file)

insert_records = "INSERT INTO ingredient (id, name, icalories, protein, carbs, fat, fiber, sugar, item_unit_size, item_price, u_price, aisle_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM ingredient"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)
connection.commit()

# Import UnitIngredient
file = open("unitingredient.csv")

contents = csv.reader(file)

insert_records = (
    "INSERT INTO unit_ingredient (id, iid, uid, multiplyer) VALUES(?, ?, ?, ?)"
)

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM unit_ingredient"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)
connection.commit()

connection.close()
