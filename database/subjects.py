from database.connection import get_connection


def add_subject(name: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Subjects (name) VALUES (?)
    """, (name,))

    connection.commit()

    cursor.execute("SELECT SCOPE_IDENTITY()")
    subject_id = int(cursor.fetchone()[0])

    connection.close()

    return {
        "id": subject_id,
        "name": name
    }


def get_subjects():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject_id, name
        FROM Subjects
        ORDER BY name
    """)

    rows = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "name": row[1]
        }
        for row in rows
    ]


def delete_subject(subject_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM Subjects
        WHERE subject_id = ?
    """, (subject_id,))

    connection.commit()

    success = cursor.rowcount > 0

    connection.close()

    return success


def get_subject_by_id(subject_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject_id, name
        FROM Subjects
        WHERE subject_id = ?
    """, (subject_id,))

    row = cursor.fetchone()

    connection.close()

    if row:
        return {
            "id": row[0],
            "name": row[1]
        }

    return None


def format_subjects_list(subjects):
    if not subjects:
        return "📭 Список предметов пуст"

    result = "📚 Список предметов:\n\n"

    for subject in subjects:
        result += f"• {subject['name']}\n"

    return result