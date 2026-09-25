import os
import sqlite3
import hashlib

DB_PATH = "ishara.db"


def _connect():
    return sqlite3.connect(DB_PATH)


def init_db():
    with _connect() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)

        con.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                sign TEXT NOT NULL,
                text TEXT NOT NULL,
                confidence REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        con.commit()


def _hash(password):
    salt = os.getenv(
        "ISHARA_PASSWORD_SALT",
        "ishara-local-salt"
    )

    return hashlib.sha256(
        (salt + password).encode()
    ).hexdigest()


def register_user(name, email, password):

    name = name.strip()
    email = email.strip().lower()

    if not name or not email:
        return False, "Name and email are required."

    if len(password) < 6:
        return False, "Password must contain at least 6 characters."

    try:

        with _connect() as con:

            con.execute(
                """
                INSERT INTO users
                (name, email, password_hash)
                VALUES (?, ?, ?)
                """,
                (
                    name,
                    email,
                    _hash(password)
                )
            )

            con.commit()

        return True, "Account created successfully."

    except sqlite3.IntegrityError:

        return False, "This email is already registered."


def authenticate_user(email, password):

    email = email.strip().lower()

    with _connect() as con:

        row = con.execute(
            """
            SELECT id, name, email
            FROM users
            WHERE email = ?
            AND password_hash = ?
            """,
            (
                email,
                _hash(password)
            )
        ).fetchone()

    if row:

        return {
            "id": row[0],
            "name": row[1],
            "email": row[2]
        }

    return None
