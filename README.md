# Sistema Biblioteca

Sistema desktop para gerenciamento de bibliotecas escolares, desenvolvido com Python, CustomTkinter e SQLite.

O projeto foi criado com foco em simplicidade, organização e facilidade de uso, permitindo o controle completo de livros, alunos e empréstimos através de uma interface moderna e intuitiva.

---

# Funcionalidades

## Livros

- Cadastro de livros
- Edição e remoção de registros
- Controle de quantidade disponível
- Controle de disponibilidade
- Pesquisa de livros
- Informações de:
  - autor
  - categoria
  - editora
  - observações

---

## Alunos

- Cadastro de alunos
- Controle de matrícula
- Controle de turma
- Pesquisa de alunos
- Ativação/desativação de alunos

---

## Empréstimos

- Registro de empréstimos
- Registro de devoluções
- Controle automático de disponibilidade
- Histórico de empréstimos
- Controle de datas:
  - empréstimo
  - devolução prevista
  - devolução realizada

---

# Tecnologias Utilizadas

- Python 3
- CustomTkinter
- SQLAlchemy
- SQLite
- PyInstaller

---

# Interface

O sistema utiliza uma interface gráfica moderna baseada em CustomTkinter, com estrutura semelhante a sistemas ERP administrativos.

---

# Estrutura do Projeto

```txt
sistema_biblioteca/
│
├── app.py
├── database/
├── models/
├── views/
├── assets/
└── requirements.txt