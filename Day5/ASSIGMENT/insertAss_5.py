import pymysql
# Multi data added to table

schema_name = "mydb"
# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

query = "INSERT into mydb.Dogs (NAME, AGE,BREED) values (%s,%s,%s);"
records = [
    ('joe', 2, 'mongural'),
    ('james', 4, 'mongural'),
    ('kem', 2, 'mongural')
]
# Inserting data into table
cursor.executemany(query, records)
print(cursor.rowcount, "record in table")
cursor.close()
conn.close()
