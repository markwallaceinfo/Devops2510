import pymysql

schema_name = "mydb"
conn = None
def connect_to_db():

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)


    # Getting a cursor from Database
    cursor = conn.cursor()
def create_table():
    # Inserting data into table
    statementToExecute = "CREATE TABLE `" + schema_name + ("`.`users`(`user_id` PRIMARY KEY, INT NOT NULL,`user_name` "
                                                           "VARCHAR(50) NOT NULL,'creation_date'VARCHAR(50));")
    cursor.execute(statementToExecute)
    cursor.close()
    conn.close
