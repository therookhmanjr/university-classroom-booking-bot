
from database.connection import get_connection


def create_booking(
        classroom_id,
        user_id,
        booking_date,
        start_time,
        end_time,
        purpose,
        status="Pending"
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Booking
        (
            classroom_id,
            user_id,
            booking_date,
            start_time,
            end_time,
            purpose,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        classroom_id,
        user_id,
        booking_date,
        start_time,
        end_time,
        purpose,
        status
    ))

    connection.commit()
    connection.close()


def get_user_bookings(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM Booking
        WHERE user_id = ?
    """, (user_id,))

    bookings = cursor.fetchall()

    connection.close()

    return bookings


def cancel_booking(booking_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE Booking
        SET status = 'Cancelled'
        WHERE booking_id = ?
    """, (booking_id,))

    connection.commit()
    connection.close()
