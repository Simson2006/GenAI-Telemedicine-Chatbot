import sqlite3
import ast

DB_FILE="chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                    phone_number TEXT PRIMARY KEY,
                    message_history TEXT
                )''')
    conn.commit()
    conn.close()


def get_message_history(phone_number):
    init_db()

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Check if phone number exists
    c.execute("SELECT message_history FROM chat_history WHERE phone_number=?", (phone_number,))
    row = c.fetchone()

    if row is None:
        # Phone number not exist → insert empty history
        c.execute(
            "INSERT INTO chat_history (phone_number, message_history) VALUES (?, ?)",
            (phone_number, "")
        )
        conn.commit()
        chat_history = []
    else:

        msg_str = row[0]
        if msg_str:
            chat_history = ast.literal_eval(msg_str)
        else:
            chat_history = []

    conn.close()

    return chat_history


def save_message_history(phone_number, chat_history):
    # Ensure DB/table exists
    init_db()

    # Convert Python list to string
    chat_history_str = str(chat_history)

    # Save into DB (insert if new, replace if exists)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "REPLACE INTO chat_history (phone_number, message_history) VALUES (?, ?)",
        (phone_number, chat_history_str)
    )

    conn.commit()
    conn.close()