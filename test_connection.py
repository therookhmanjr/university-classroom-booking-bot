from database.connection import get_connection

try:
    conn = get_connection()
    print("Подключение успешно!")

    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")

    print(cursor.fetchone()[0])

    conn.close()

except Exception as e:
    print(e)