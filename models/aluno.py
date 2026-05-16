# models/aluno.py

from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255), nullable=False)

    turma = Column(String(100), nullable=False)

    matricula = Column(String(100), unique=True)

    telefone = Column(String(30))

    ativo = Column(Boolean, default=True)