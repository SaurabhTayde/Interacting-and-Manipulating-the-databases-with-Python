# You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".


import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))  # We are using below command since this command is not safe considering SQL injection due to hackers
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

#insert("Coffee Cup", 10, 5)

def view():
    conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#insert('Apple', 10, 15)
#insert('Orange', 10, 15)
print(view())
#delete("Orange")
#print(view())
update(20,15,'Apple')
print(view())
