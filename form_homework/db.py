import sqlite3

conn = sqlite3.connect('yichun.db')
print ("Opened database successfully")

#conn.execute('CREATE TABLE user (name TEXT, email TEXT, password TEXT)')

#conn.execute('DROP TABLE form_collection6')
#conn.execute('CREATE TABLE form_collection4 (first_name TEXT, last_name TEXT, email TEXT, password TEXT, gender TEXT, order_type TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT, message TEXT, check TEXT)')
conn.execute(' CREATE TABLE form_collection6 (first_name TEXT, last_name TEXT, email TEXT, password TEXT, gender TEXT, order_type TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT, checkbox TEXT, message TEXT, photo TEXT)')

#conn.execute(' CREATE TABLE photo (photo BLOB)')

'''
cur = conn.cursor()
conn.execute('SELECT * FROM  form_collection2 ')
rows = cur.fetchall()
for row in rows:
    print(row)
    '''
print ("create form_collection1")
print("Table created successfully")
conn.close()
