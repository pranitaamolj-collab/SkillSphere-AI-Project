import sqlite3

DB_NAME = "skillsphere.db"


def get_connection():

    return sqlite3.connect(DB_NAME)


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'Employee'
        )
    """)

    conn.commit()
    conn.close()


def add_user(
    name,
    email,
    password,
    role="Employee"
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO users
            (name, email, password, role)
            VALUES (?, ?, ?, ?)
        """, (
            name,
            email,
            password,
            role
        ))

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def check_user(
    email,
    password
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, role
        FROM users
        WHERE email = ? AND password = ?
    """, (
        email,
        password
    ))

    user = cursor.fetchone()

    conn.close()

    return user


def get_all_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, role
        FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    return users