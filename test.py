import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# CREATE TABLE WITH ID, USERNAME AND PASSWORD
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'rishav', '123456')
# INSERT VALUE TO TABLE QUERY
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'ashish', '123456'),
    (3, 'ayush', '123456'),
]
cursor.executemany(insert_query, users)

# EXTRACT VALUES FROM DATABASE
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# commit only when we add data to db
connection.commit()
connection.close()
