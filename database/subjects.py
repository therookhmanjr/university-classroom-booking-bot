from database.connection import get_connection

def add_subject(name: str) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Subjects (name) VALUES (?)
    """, (name,))

    connection.commit()
    connection.close()

def get_subjects():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM Subjects
    """)

    subjects = cursor.fetchall()

    connection.close()

    return subjects