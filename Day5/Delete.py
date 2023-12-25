
import pymysql

schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

cursor.execute(f"DELETE FROM {schema_name}.Dogs WHERE name = 'kem'")

cursor.close()
conn.close()
