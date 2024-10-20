from multiprocessing import connection
import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)

def get_airport_info():
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return (result)

code = input("Enter the area code: ")
count = get_airport_info(code)
if count is not None:
    print(f"{code} has: {count} airports")
else:
    print(f"No airports in {code}")

conn.close()