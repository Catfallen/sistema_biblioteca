# views/pages/dashboard_page.py

import customtkinter as ctk
from tkinter import ttk

from sqlalchemy import text

from database.database import SessionLocal


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.session = SessionLocal()

        self.pack(fill="both", expand=True)

        self.criar_interface()

        self.carregar_dados()

    def criar_interface(self):

         # ---------------- SCROLL ----------------

        self.canvas = ctk.CTkCanvas(self, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(self, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.scroll_frame = ctk.CTkFrame(self.canvas)

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scroll_frame,
            anchor="nw"
        )

        self.scroll_frame.bind("<Configure>", self.atualizar_scroll)
        self.canvas.bind("<Configure>", self.atualizar_largura)

        # captura o scroll em qualquer lugar da janela
        self.winfo_toplevel().bind_all(
    "<MouseWheel>",
    self.scroll_mouse
)

        # ---------------- TÍTULO ----------------

        titulo = ctk.CTkLabel(
            self.scroll_frame,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        titulo.pack(pady=30)

        # ---------------- CARDS ----------------

        cards_frame = ctk.CTkFrame(self.scroll_frame)
        cards_frame.pack(fill="x", padx=10, pady=10)

        self.card_alunos = self.criar_card(cards_frame, "Alunos")
        self.card_livros = self.criar_card(cards_frame, "Livros")
        self.card_emprestimos = self.criar_card(cards_frame, "Empréstimos")
        self.card_atrasados = self.criar_card(cards_frame, "Atrasados")

        self.card_alunos.grid(row=0, column=0, padx=10, pady=10)
        self.card_livros.grid(row=0, column=1, padx=10, pady=10)
        self.card_emprestimos.grid(row=0, column=2, padx=10, pady=10)
        self.card_atrasados.grid(row=0, column=3, padx=10, pady=10)

        # ---------------- TABELAS ----------------

        self.top_livros = self.criar_tabela(
            "Livros Mais Emprestados",
            ("Livro", "Total")
        )

        self.top_alunos = self.criar_tabela(
            "Alunos que Mais Retiram",
            ("Aluno", "Total")
        )

        self.emprestados = self.criar_tabela(
            "Livros Emprestados",
            ("Livro", "Aluno", "Devolver Em")
        )

        self.atrasados = self.criar_tabela(
            "Empréstimos Atrasados",
            ("Livro", "Aluno", "Dias")
        )

        self.sem_movimento = self.criar_tabela(
            "Livros Sem Movimentação",
            ("Livro",)
        )
    def scroll_mouse(self, event):

        print("scroll", event.delta)

        self.canvas.yview_scroll(
            -int(event.delta / 120),
            "units"
        )
    def atualizar_scroll(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def atualizar_largura(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)


    def criar_card(self, parent, titulo):

        frame = ctk.CTkFrame(parent, width=180, height=100)

        ctk.CTkLabel(
            frame,
            text=titulo,
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 5))

        valor = ctk.CTkLabel(
            frame,
            text="0",
            font=("Arial", 24)
        )

        valor.pack()

        frame.valor = valor

        return frame

    def criar_tabela(self, titulo, colunas):

        frame = ctk.CTkFrame(self.scroll_frame)
        frame.pack(fill="both", expand=False, padx=10, pady=10)

        ctk.CTkLabel(
            frame,
            text=titulo,
            font=("Arial", 18, "bold")
        ).pack(pady=5)

        tree = ttk.Treeview(
            frame,
            columns=colunas,
            show="headings",
            height=8
        )

        for coluna in colunas:
            tree.heading(coluna, text=coluna)
            tree.column(coluna, width=200)

        tree.pack(fill="x", padx=10, pady=10)
        #tree.bind("<MouseWheel>", self.scroll_mouse)
        tree.bind(
    "<MouseWheel>",
    self.scroll_mouse,
    add="+"
)

        return tree

    def carregar_dados(self):

        self.carregar_cards()

        self.carregar_livros_mais_emprestados()

        self.carregar_alunos_mais_ativos()

        self.carregar_emprestados()

        self.carregar_atrasados()

        self.carregar_sem_movimento()

    def carregar_cards(self):

        total_alunos = self.session.execute(text("""
            SELECT COUNT(*)
            FROM alunos
            WHERE ativo = 1
        """)).scalar() or 0

        total_livros = self.session.execute(text("""
            SELECT COUNT(*)
            FROM livros
        """)).scalar() or 0

        total_emprestimos = self.session.execute(text("""
            SELECT COUNT(*)
            FROM emprestimos
            WHERE UPPER(status) = 'EMPRESTADO'
        """)).scalar() or 0

        total_atrasados = self.session.execute(text("""
            SELECT COUNT(*)
            FROM emprestimos
            WHERE UPPER(status) = 'EMPRESTADO'
            AND DATE(data_devolucao_prevista) < DATE('now')
        """)).scalar() or 0

        self.card_alunos.valor.configure(text=str(total_alunos))
        self.card_livros.valor.configure(text=str(total_livros))
        self.card_emprestimos.valor.configure(text=str(total_emprestimos))
        self.card_atrasados.valor.configure(text=str(total_atrasados))


    def limpar_tree(self, tree):

        for item in tree.get_children():
            tree.delete(item)


    def carregar_livros_mais_emprestados(self):

        self.limpar_tree(self.top_livros)

        dados = self.session.execute(text("""
            SELECT
                l.obra,
                COUNT(e.id) AS total
            FROM livros l
            INNER JOIN emprestimos e
                ON e.id_livro = l.id
            GROUP BY l.id, l.obra
            ORDER BY total DESC, l.obra
            LIMIT 10
        """)).fetchall()

        for obra, total in dados:
            self.top_livros.insert(
                "",
                "end",
                values=(obra, total)
            )


    def carregar_alunos_mais_ativos(self):

        self.limpar_tree(self.top_alunos)

        dados = self.session.execute(text("""
            SELECT
                a.nome,
                COUNT(e.id) AS total
            FROM alunos a
            INNER JOIN emprestimos e
                ON e.id_aluno = a.id
            GROUP BY a.id, a.nome
            ORDER BY total DESC, a.nome
            LIMIT 10
        """)).fetchall()

        for nome, total in dados:
            self.top_alunos.insert(
                "",
                "end",
                values=(nome, total)
            )


    def carregar_emprestados(self):

        self.limpar_tree(self.emprestados)

        dados = self.session.execute(text("""
            SELECT
                l.obra,
                a.nome,
                e.data_devolucao_prevista
            FROM emprestimos e
            INNER JOIN livros l
                ON l.id = e.id_livro
            INNER JOIN alunos a
                ON a.id = e.id_aluno
            WHERE UPPER(e.status) = 'EMPRESTADO'
            ORDER BY e.data_devolucao_prevista
        """)).fetchall()

        for obra, aluno, data in dados:
            self.emprestados.insert(
                "",
                "end",
                values=(obra, aluno, data)
            )


    def carregar_atrasados(self):

        self.limpar_tree(self.atrasados)

        dados = self.session.execute(text("""
            SELECT
                l.obra,
                a.nome,
                CAST(
                    JULIANDAY(DATE('now')) -
                    JULIANDAY(DATE(e.data_devolucao_prevista))
                    AS INTEGER
                ) AS dias_atraso
            FROM emprestimos e
            INNER JOIN livros l
                ON l.id = e.id_livro
            INNER JOIN alunos a
                ON a.id = e.id_aluno
            WHERE UPPER(e.status) = 'EMPRESTADO'
            AND DATE(e.data_devolucao_prevista) < DATE('now')
            ORDER BY dias_atraso DESC
        """)).fetchall()

        for obra, aluno, dias_atraso in dados:
            self.atrasados.insert(
                "",
                "end",
                values=(obra, aluno, dias_atraso)
            )


    def carregar_sem_movimento(self):

        self.limpar_tree(self.sem_movimento)

        dados = self.session.execute(text("""
            SELECT l.obra
            FROM livros l
            WHERE NOT EXISTS (
                SELECT 1
                FROM emprestimos e
                WHERE e.id_livro = l.id
            )
            ORDER BY l.obra
        """)).fetchall()

        for (obra,) in dados:
            self.sem_movimento.insert(
                "",
                "end",
                values=(obra,)
            )