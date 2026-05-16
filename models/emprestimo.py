# models/emprestimo.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.database import Base


class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)

    id_livro = Column(
        Integer,
        ForeignKey("livros.id"),
        nullable=False
    )

    id_aluno = Column(
        Integer,
        ForeignKey("alunos.id"),
        nullable=False
    )

    data_emprestimo = Column(Date, nullable=False)

    data_devolucao_prevista = Column(Date)

    data_devolucao = Column(Date)

    status = Column(
        String(50),
        default="emprestado"
    )

    livro = relationship("Livro")

    aluno = relationship("Aluno")