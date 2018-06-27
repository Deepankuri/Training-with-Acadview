#Question1
"""
We start by installing and then importing mysql module in python.
We will enter simple commands to create table in the database.
"""
import mysql.connector

username = 'Deepankuri'
password = 'xxxxxx'
host = 'localhost'
db = 'Deepankuri'

x = pymysql.connect(host, username, password)
x.select_db('Deepankuri')
cursor = x.cursor()

table1 = '''CREATE TABLE authors(author_id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY, first_name VARCHAR(50) NOT NULL, middle_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL  )'''
cursor.execute(table1)
table2 = '''CREATE TABLE zipcodes(zip_id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY, city VARCHAR(50) NOT NULL, state VARCHAR(50) NOT NULL, zip_code(50) NOT NULL  )'''
cursor.execute(table2)
table3 = '''CREATE TABLE publishers(pub_id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, street_add VARCHAR(50) NOT NULL, FOREIGN KEY(zip_id) REFERENCES zipcodes(zip_id) )'''
cursor.execute(table3)
table4 = '''CREATE TABLE titles(title_id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY, title VARCHAR(50) NOT NULL, isbn INT(50) NOT NULL, publisher_id INT(50) NOT NULL, pub_year INT(50) NOT NULL, FOREIGN KEY(publisher_id) REFERENCES publishers(pub_id )'''
cursor.execute(table4)
table5  = '''CREATE TABLE book(book_id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY, title_id  INT(50) NOT NULL, location VARCHAR(50) NOT NULL, genre VARCHAR(50) NOT NULL, FOREIGN KEY(title_id) REFERENCES titles(title_id)  )'''
cursor.execute(table5)
table6 = '''CREATE TABLE authortitles(author_title_id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY, author_id  INT(50) NOT NULL, title_id INT(50) NOT NULL, FOREIGN KEY(author_id) REFERENCES authors(author_id), FOREIGN KEY(title_id) REFERENCES titles(title_id)  )'''
cursor.execute(table6)

"""
The tables have been created and our database is ready hence.
"""

#Question2
"""
Now we will insert values into these tables.
"""
req1 = '''INSERT INTO authors(author_id, first_name, middle_name, last_name) VALUES ('1235', 'stephen', 'william', 'hawking');'''
req2 = '''INSERT INTO zipcodes(zip_id, city, state, zip_code) VALUES ('3325', 'gurugram', 'hry', '13002' );'''
req3 = '''INSERT INTO publishers(pub_id, street_add, zip_id) VALUES ('1142', 'b.s. nagar, shanta road', '3325');'''
req4 = '''INSERT INTO titles(title_id, title, isbn, publisher_id , pub_year) VALUES ('890', 'a brief hostory of time', '1142', '1998');'''

x.commit()
print(cursor.fetchall())

#Question3
"""
Updating the values in the table
"""
update_req = """UPDATE titles SET isbn = '45668' where title = 'a brief hostory of time' """
print('before the updation since we didnt commit')
print(cursor.fetchall())
x.commit()
print('updated now')
print(cursor.fetchall())