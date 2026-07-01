from database.connection import get_connection

def register_user(telegram_id: int, full_name:str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO Users (telegram_id, full_name, role) VALUES (?, ?, ?)
        """, (telegram_id, full_name, "User")
    )


def add_user(telegram_id: int, full_name: str, role: str) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Users (telegram_id, full_name, role)
        VALUES (?, ?, ?)
    """, (telegram_id, full_name, role))

    connection.commit()
    connection.close()

def get_user(telegram_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM Users
        WHERE telegram_id = ?
    """, (telegram_id))

    user = cursor.fetchone()

    connection.close()

    return user

def get_all_users():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Users""")
        return cursor.fetchall()
    finally:
        connection.close()


def delete_user(telegram_id: int) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM Users WHERE telegram_id = ?
    """, (telegram_id))

    connection.commit()
    connection.close()

