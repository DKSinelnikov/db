import sqlite3
from datetime import datetime


def add_message(id: int, message: str) -> None:
    connection = sqlite3.connect("vitte_bot.sqlite3")
    cursor = connection.cursor()
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    cursor.execute("INSERT INTO messages (id, message, datetime) VALUES (?, ?, ?)", (id, message, now))
    connection.commit()


