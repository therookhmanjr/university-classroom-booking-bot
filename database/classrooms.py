from database.connection import get_connection


def get_all_classrooms():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM Classrooms
    """)

    classrooms = cursor.fetchall()

    connection.close()

    return classrooms

def get_classroom_by_number(room_number):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
            SELECT classroom_id FROM Classrooms WHERE room_number = ?
        """, (room_number,)
    )

    classroom = cursor.fetchone()

    connection.close()

    return classroom

def get_free_classrooms():
    pass
