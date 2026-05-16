# database/migrations/migration_manager.py

from sqlalchemy import text
from database.database import engine


def create_migrations_table():
    with engine.connect() as conn:

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                version TEXT UNIQUE
            )
        """))

        conn.commit()


def migration_executed(version):

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT version
                FROM migrations
                WHERE version = :version
            """),
            {"version": version}
        ).fetchone()

        return result is not None


def register_migration(version):

    with engine.connect() as conn:

        conn.execute(
            text("""
                INSERT INTO migrations(version)
                VALUES(:version)
            """),
            {"version": version}
        )

        conn.commit()