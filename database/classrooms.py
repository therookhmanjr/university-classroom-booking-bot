
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


def get_free_classrooms():
    pass
