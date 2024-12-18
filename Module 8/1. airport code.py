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

def get_airport_by_ident(icao):
    sql = f"Select airport.name, airport.municipality from airport where ident = '{icao}'"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return (result)

code = input("Enter ICAO code: ")
airport = get_airport_by_ident(code)
if airport is not None:
    print(f"{airport} is located")
else:
    print("not found")

conn.close()
