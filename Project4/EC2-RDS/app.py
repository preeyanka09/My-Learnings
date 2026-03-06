import pymysql

host = "database-1.c07m8igqcg94.us-east-1.rds.amazonaws.com"
user = "admin"
password = "admin123"
database = "aws"

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=3306
    )

    print("Connected to RDS MySQL!")

    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES;")

    for db in cursor.fetchall():
        print(db)


    cursor.execute("SELECT * FROM learners;")
    rows = cursor.fetchall()

    print("Rows under the table are as follows")
    for row in rows:
         print(row)

    connection.close()

except Exception as e:
    print("Connection failed:", e)
