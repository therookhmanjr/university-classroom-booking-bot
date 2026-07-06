# database/subjects.py

from database.connection import get_connection
from typing import List, Dict, Optional


def get_subjects() -> List[Dict]:
    """
    Получить список всех предметов

    Returns:
        List[Dict]: Список словарей с предметами (id, name)
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM Subjects
    """)

    subjects = cursor.fetchall()
    connection.close()

    # Преобразуем результат в список словарей
    result = []
    for subject in subjects:
        result.append({
            "id": subject[0],  # предполагаем, что id - первый столбец
            "name": subject[1]  # предполагаем, что name - второй столбец
        })

    return result


def get_subject_by_id(subject_id: int) -> Optional[Dict]:
    """
    Получить предмет по ID

    Args:
        subject_id: ID предмета

    Returns:
        Optional[Dict]: Словарь с данными предмета или None
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM Subjects WHERE id = ?
    """, (subject_id,))

    subject = cursor.fetchone()
    connection.close()

    if subject:
        return {
            "id": subject[0],
            "name": subject[1]
        }
    return None


def add_subject(name: str) -> Dict:
    """
    Добавить новый предмет

    Args:
        name: Название предмета

    Returns:
        Dict: Созданный предмет с ID
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Subjects (name) VALUES (?)
    """, (name,))

    connection.commit()

    # Получаем ID добавленного предмета
    subject_id = cursor.lastrowid

    connection.close()

    return {"id": subject_id, "name": name}


def delete_subject(subject_id: int) -> bool:
    """
    Удалить предмет по ID

    Args:
        subject_id: ID предмета для удаления

    Returns:
        bool: True - удалено, False - предмет не найден
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Сначала проверяем, существует ли предмет
    cursor.execute("""
        SELECT id FROM Subjects WHERE id = ?
    """, (subject_id,))

    exists = cursor.fetchone()

    if not exists:
        connection.close()
        return False

    # Удаляем предмет
    cursor.execute("""
        DELETE FROM Subjects WHERE id = ?
    """, (subject_id,))

    connection.commit()
    connection.close()

    return True


def format_subjects_list(subjects: List[Dict]) -> str:
    """
    Форматирует список предметов для вывода пользователю

    Args:
        subjects: Список предметов

    Returns:
        str: Отформатированная строка
    """
    if not subjects:
        return "📭 Список предметов пуст"

    result = "📚 <b>Список предметов:</b>\n\n"
    for subject in subjects:
        result += f"• {subject['name']}\n"

    return result