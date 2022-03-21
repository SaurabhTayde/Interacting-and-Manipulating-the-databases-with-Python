# SQLite database is not client server database. It is embedded into the end program. It is based on file.
# All the data in GUI (developed locally) is stored in .DB file.
# And this code can be given to anyone not having SQLit installed and they can use this program (They can update, delete data as well)
# But in PostgreSQL database,  the user you are giving your program should have PostgreSQL installed
# So, SQLit is small database and it's portable.
# And PostgreSQL is appropriate for web application. If you are getting some data from user from website,
# You store your data on a PostgreSQL database on your server and Python is the program that gets this data from client on the browser and sends those data in your database

# Python libraries:
# sqlite3 for SQLite database
# psycopg2 for PostgreSQL

# Interaction with SQLite databse:

# Standard process of interacgting with databases is as follows:
# 1. Connect a database
# 2. Create cursor object (pointer to access rows from a table for database)
# 3. Write a SQL query
# 4. Commit changes
# 5. Close the connection


import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

#insert("Coffee Cup", 10, 5)

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()

update(11,6,'Water Glass')
delete('Wine Glass')

print(view())
