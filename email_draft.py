import sqlite3


def setup_database():
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        receiver TEXT,
        subject TEXT,
        body TEXT,
        status TEXT
    )
    """)


    conn.commit()
    conn.close()


def create_draft(receiver, subject, body):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emails(receiver, subject, body, status)
    VALUES (?, ?, ?, ?)
    """, (receiver, subject, body, "draft"))

    conn.commit()
    conn.close()

    print("Draft saved successfully")


def show_drafts():
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, receiver, subject
    FROM emails
    WHERE status = ?
    """, ("draft",))

    drafts = cursor.fetchall()

    if len(drafts) == 0:
        print("No drafts available")

    else:
        print("\nYour drafts:")
        for draft in drafts:
            print(f"ID: {draft[0]}")
            print(f"To: {draft[1]}")
            print(f"Subject: {draft[2]}")
            print("--------------------")

    conn.close()


def mark_sent(id):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE emails
    SET status = ?
    WHERE id = ?
    """, ("sent", id))

    conn.commit()
    conn.close()

def get_draft(id):
    conn = sqlite3.connect("jarvis.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT receiver, subject, body
    FROM emails
    WHERE id = ? AND status = ?
    """, (id, "draft"))

    draft = cursor.fetchone()

    conn.close()

    if draft is None:
        print("Draft not found")
        return None

    return draft