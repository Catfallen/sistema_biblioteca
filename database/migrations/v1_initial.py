# database/migrations/v1_initial.py

from database.database import Base, engine

from models.livro import Livro
from models.aluno import Aluno
from models.emprestimo import Emprestimo

from database.migrations.migration_manager import (
    create_migrations_table,
    migration_executed,
    register_migration
)


VERSION = "v1_initial"


def upgrade():

    create_migrations_table()

    if migration_executed(VERSION):
        print("Migração já executada.")
        return

    Base.metadata.create_all(bind=engine)

    register_migration(VERSION)

    print("Migração v1 executada com sucesso.")


if __name__ == "__main__":
    upgrade()