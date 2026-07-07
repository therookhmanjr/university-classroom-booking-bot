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

def delete_subject(subject_id: int) -> None:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM Subjects WHERE subject_id = ?
    """, (subject_id,))
    connection.commit()
    connection.close()

def get_subject_by_id(subject_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM Subjects WHERE subject_id = ?
    """, (subject_id,))
    subject = cursor.fetchone()
    connection.close()
    return subject