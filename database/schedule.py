
from database.connection import get_connection


def get_schedule():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM Schedule
    """)

    schedule = cursor.fetchall()

    connection.close()

    return schedule


def add_schedule(
        subject_id,
        classroom_id,
        teacher_id,
        lesson_date,
        start_time,
        end_time,
        group_name
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Schedule
        (
            subject_id,
            classroom_id,
            teacher_id,
            lesson_date,
            start_time,
            end_time,
            group_name
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        subject_id,
        classroom_id,
        teacher_id,
        lesson_date,
        start_time,
        end_time,
        group_name
    ))

    connection.commit()
    connection.close()
