import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        create_query = """CREATE TABLE IF NOT EXISTS employees(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100),
                            department VARCHAR(100)
                          );"""
        cursor.execute(create_query)

        insert_query = "INSERT INTO employees(name, department) VALUES (%s, %s)"
        values = [("John", "IT"), ("Amar", "PROD"), ("Ajay", "ADMIN")]
        cursor.executemany(insert_query, values)
        connection.commit()

        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()

        for row in result:
            print(row)

except Exception as e:
    print("Error:", e)


finally:
    connection.close()



