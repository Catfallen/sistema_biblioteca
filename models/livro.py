# models/livro.py

from sqlalchemy import Column, Integer, String
from database.database import Base


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)

    obra = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)

    ano = Column(Integer)

    categoria = Column(String(100))

    editora = Column(String(150))

    quantidade = Column(Integer, default=1)

    observacao = Column(String(500))

    status = Column(String(50), default="disponivel")