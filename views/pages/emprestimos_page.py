# views/emprestimos_page.py

import customtkinter as ctk

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date, timedelta, datetime

from sqlalchemy.orm import joinedload

from database.database import SessionLocal

from models.emprestimo import Emprestimo
from models.livro import Livro
from models.aluno import Aluno


class EmprestimosPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.session = SessionLocal()

        self.emprestimo_selecionado_id = None

        self.configure(fg_color="transparent")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.criar_header()

        self.criar_formulario()

        self.criar_tabela()

        self.carregar_dados()

        self.listar_emprestimos()

    # =========================================================
    # HEADER
    # =========================================================

    def criar_header(self):

        header = ctk.CTkFrame(
            self,
            height=80
        )

        header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=20
        )

        titulo = ctk.CTkLabel(
            header,
            text="Gerenciamento de Empréstimos",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            side="left",
            padx=20,
            pady=20
        )

    # =========================================================
    # FORMULÁRIO
    # =========================================================

    def criar_formulario(self):

        form_frame = ctk.CTkFrame(
            self,
            width=350
        )

        form_frame.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(20, 10),
            pady=(0, 20)
        )

        titulo_form = ctk.CTkLabel(
            form_frame,
            text="Novo Empréstimo",
            font=("Arial", 22, "bold")
        )

        titulo_form.pack(
            pady=(20, 20)
        )

       # =====================================================
        # Livro
        # =====================================================

        livro_label = ctk.CTkLabel(
            form_frame,
            text="Livro"
        )

        livro_label.pack(
            anchor="w",
            padx=20
        )

        self.livro_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Pesquisar livro..."
        )

        self.livro_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 5)
        )

        self.livro_listbox = tk.Listbox(
            form_frame,
            height=5
        )
        self.livro_listbox.bind(
        "<<ListboxSelect>>",
        self.selecionar_livro_lista
        )

        self.livro_listbox.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.livro_entry.bind(
            "<KeyRelease>",
            self.pesquisar_livros
        )

                # =====================================================
        # Aluno
        # =====================================================

        aluno_label = ctk.CTkLabel(
            form_frame,
            text="Aluno"
        )

        aluno_label.pack(
            anchor="w",
            padx=20
        )

        self.aluno_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Pesquisar aluno..."
        )

        self.aluno_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 5)
        )

        self.aluno_listbox = tk.Listbox(
            form_frame,
            height=5
        )

        self.aluno_listbox.bind(
            "<<ListboxSelect>>",
            self.selecionar_aluno_lista
        )

        self.aluno_listbox.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.aluno_entry.bind(
            "<KeyRelease>",
            self.pesquisar_alunos
        )
        # Data empréstimo

        data_emp_label = ctk.CTkLabel(
            form_frame,
            text="Data empréstimo"
        )

        data_emp_label.pack(
            anchor="w",
            padx=20
        )

        self.data_emprestimo_entry = ctk.CTkEntry(
            form_frame
        )

        self.data_emprestimo_entry.insert(
            0,
            date.today().strftime("%d/%m/%Y")
        )

        self.data_emprestimo_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # Data devolução prevista

        devolucao_label = ctk.CTkLabel(
            form_frame,
            text="Data devolução prevista"
        )

        devolucao_label.pack(
            anchor="w",
            padx=20
        )

        self.data_devolucao_prevista_entry = ctk.CTkEntry(
            form_frame
        )

        self.data_devolucao_prevista_entry.insert(
            0,
            (
                date.today() + timedelta(days=7)
            ).strftime("%d/%m/%Y")
        )

        self.data_devolucao_prevista_entry.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        # Botão emprestar

        self.salvar_btn = ctk.CTkButton(
            form_frame,
            text="Registrar Empréstimo",
            height=42,
            command=self.registrar_emprestimo
        )

        self.salvar_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Botão devolução

        self.devolver_btn = ctk.CTkButton(
            form_frame,
            text="Registrar Devolução",
            height=42,
            fg_color="#d68c00",
            hover_color="#b57400",
            command=self.registrar_devolucao
        )

        self.devolver_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Botão excluir

        self.excluir_btn = ctk.CTkButton(
            form_frame,
            text="Excluir Registro",
            height=42,
            fg_color="#c0392b",
            hover_color="#962d22",
            command=self.excluir_emprestimo
        )

        self.excluir_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Limpar
        """
        self.limpar_btn = ctk.CTkButton(
            form_frame,
            text="Limpar",
            height=42,
            fg_color="#555555",
            hover_color="#444444",
            command=self.limpar_campos
        )

        self.limpar_btn.pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )
        """
    # =========================================================
    # TABELA
    # =========================================================

    def criar_tabela(self):

        tabela_frame = ctk.CTkFrame(self)

        tabela_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        pesquisa_frame = ctk.CTkFrame(
            tabela_frame,
            fg_color="transparent"
        )

        pesquisa_frame.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        self.pesquisa_entry = ctk.CTkEntry(
            pesquisa_frame,
            placeholder_text="Pesquisar empréstimo..."
        )

        self.pesquisa_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        pesquisar_btn = ctk.CTkButton(
            pesquisa_frame,
            text="Pesquisar",
            width=120,
            command=self.pesquisar_emprestimos
        )

        pesquisar_btn.pack(side="left")

        # Treeview

        colunas = (
            "id",
            "livro",
            "aluno",
            "emprestimo",
            "prevista",
            "devolucao",
            "status"
        )

        self.tree = ttk.Treeview(
            tabela_frame,
            columns=colunas,
            show="headings",
            height=20
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("livro", text="Livro")
        self.tree.heading("aluno", text="Aluno")
        self.tree.heading("emprestimo", text="Empréstimo")
        self.tree.heading("prevista", text="Prevista")
        self.tree.heading("devolucao", text="Devolução")
        self.tree.heading("status", text="Status")

        self.tree.column("id", width=60)
        self.tree.column("livro", width=220)
        self.tree.column("aluno", width=180)
        self.tree.column("emprestimo", width=120)
        self.tree.column("prevista", width=120)
        self.tree.column("devolucao", width=120)
        self.tree.column("status", width=120)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selecionar_emprestimo
        )

    # =========================================================
    # DADOS
    # =========================================================

    def carregar_dados(self):

        livros = self.session.query(
            Livro
        ).all()

        alunos = self.session.query(
            Aluno
        ).filter_by(
            ativo=True
        ).all()
        print(alunos)
        self.livros_map = {
            f"{livro.id} - {livro.obra}": livro.id
            for livro in livros
        }

        self.alunos_map = {
            f"{aluno.id} - {aluno.nome}": aluno.id
            for aluno in alunos
        }

    # =========================================================
    # CRUD
    # =========================================================

    def registrar_emprestimo(self):

        livro_nome = self.livro_entry.get()

        aluno_nome = self.aluno_entry.get()

        if not livro_nome or not aluno_nome:

            messagebox.showwarning(
                "Aviso",
                "Selecione livro e aluno."
            )

            return

        id_livro = self.livros_map.get(
            livro_nome
        )

        id_aluno = self.alunos_map.get(
            aluno_nome
        )

        if not id_livro or not id_aluno:

            messagebox.showerror(
                "Erro",
                "Selecione um livro e aluno válidos."
            )

            return

        livro = self.session.query(
            Livro
        ).filter_by(
            id=id_livro
        ).first()

        if livro.quantidade <= 0:

            messagebox.showerror(
                "Erro",
                "Livro indisponível."
            )

            return

        data_emprestimo = datetime.strptime(
            self.data_emprestimo_entry.get(),
            "%d/%m/%Y"
        ).date()

        data_prevista = datetime.strptime(
            self.data_devolucao_prevista_entry.get(),
            "%d/%m/%Y"
        ).date()

        emprestimo = Emprestimo(
            id_livro=id_livro,
            id_aluno=id_aluno,
            data_emprestimo=data_emprestimo,
            data_devolucao_prevista=data_prevista,
            status="emprestado"
        )

        livro.quantidade -= 1

        if livro.quantidade <= 0:
            livro.status = "indisponivel"

        self.session.add(emprestimo)

        self.session.commit()

        self.listar_emprestimos()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Empréstimo registrado."
        )

    def listar_emprestimos(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        emprestimos = self.session.query(
            Emprestimo
        ).options(
            joinedload(Emprestimo.livro),
            joinedload(Emprestimo.aluno)
        ).all()

        for emp in emprestimos:

            devolucao = ""

            if emp.data_devolucao:
                devolucao = emp.data_devolucao.strftime(
                    "%d/%m/%Y"
                )

            self.tree.insert(
                "",
                "end",
                values=(
                    emp.id,
                    emp.livro.obra if emp.livro else "Livro removido",
                    emp.aluno.nome if emp.aluno else "Aluno removido",
                    emp.data_emprestimo.strftime("%d/%m/%Y"),
                    emp.data_devolucao_prevista.strftime("%d/%m/%Y"),
                    devolucao,
                    emp.status
                )
            )

    def selecionar_emprestimo(self, event):

        selecionado = self.tree.selection()

        if not selecionado:
            return

        dados = self.tree.item(
            selecionado[0]
        )["values"]

        self.emprestimo_selecionado_id = dados[0]

    def registrar_devolucao(self):

        if not self.emprestimo_selecionado_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um empréstimo."
            )

            return

        emprestimo = self.session.query(
            Emprestimo
        ).filter_by(
            id=self.emprestimo_selecionado_id
        ).first()

        if emprestimo.status == "devolvido":

            messagebox.showinfo(
                "Aviso",
                "Livro já devolvido."
            )

            return

        emprestimo.status = "devolvido"

        emprestimo.data_devolucao = date.today()

        livro = emprestimo.livro

        livro.quantidade += 1

        livro.status = "disponivel"

        self.session.commit()

        self.listar_emprestimos()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Devolução registrada."
        )

    def excluir_emprestimo(self):

        if not self.emprestimo_selecionado_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um empréstimo."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmação",
            "Deseja excluir o registro?"
        )

        if not confirmar:
            return

        emprestimo = self.session.query(
            Emprestimo
        ).filter_by(
            id=self.emprestimo_selecionado_id
        ).first()

        self.session.delete(emprestimo)

        self.session.commit()

        self.listar_emprestimos()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Registro excluído."
        )

    def pesquisar_emprestimos(self):

        termo = self.pesquisa_entry.get()

        for item in self.tree.get_children():
            self.tree.delete(item)

        emprestimos = self.session.query(
            Emprestimo
        ).options(
            joinedload(Emprestimo.livro),
            joinedload(Emprestimo.aluno)
        ).filter(
            Livro.obra.like(f"%{termo}%")
        ).all()

        for emp in emprestimos:

            devolucao = ""

            if emp.data_devolucao:
                devolucao = emp.data_devolucao.strftime(
                    "%d/%m/%Y"
                )

            self.tree.insert(
                "",
                "end",
                values=(
                    emp.id,
                    emp.livro.obra,
                    emp.aluno.nome,
                    emp.data_emprestimo.strftime("%d/%m/%Y"),
                    emp.data_devolucao_prevista.strftime("%d/%m/%Y"),
                    devolucao,
                    emp.status
                )
            )

    # =========================================================
    # UTILIDADES
    # =========================================================

    def limpar_campos(self):

        self.emprestimo_selecionado_id = None

        self.livro_combobox.set("")

        self.aluno_combobox.set("")

        self.data_emprestimo_entry.delete(0, "end")

        self.data_emprestimo_entry.insert(
            0,
            date.today().strftime("%d/%m/%Y")
        )

        self.data_devolucao_prevista_entry.delete(0, "end")

        self.data_devolucao_prevista_entry.insert(
            0,
            (
                date.today() + timedelta(days=7)
            ).strftime("%d/%m/%Y")
        )
    def pesquisar_livros(self, event=None):

        termo = self.livro_entry.get()

        self.livro_listbox.delete(0, "end")

        if not termo:
            return

        livros = self.session.query(
            Livro
        ).filter(
            Livro.obra.like(f"%{termo}%")
        ).all()

        for livro in livros:

            self.livro_listbox.insert(
                "end",
                f"{livro.id} - {livro.obra}"
            )

    def selecionar_livro_lista(self, event=None):


        selecionado = self.livro_listbox.curselection()

        if not selecionado:
            return

        valor = self.livro_listbox.get(
            selecionado[0]
        )

        self.livro_entry.delete(0, "end")

        self.livro_entry.insert(
            0,
            valor
        )

        self.livro_listbox.delete(0, "end")

        # salva o livro selecionado
        self.livro_selecionado = valor
    
    def pesquisar_alunos(self, event=None):

        termo = self.aluno_entry.get()

        self.aluno_listbox.delete(0, "end")

        if not termo:
            return

        alunos = self.session.query(
            Aluno
        ).filter(
            Aluno.nome.like(f"%{termo}%"),
            Aluno.ativo == True
        ).all()

        for aluno in alunos:

            self.aluno_listbox.insert(
                "end",
                f"{aluno.id} - {aluno.nome}"
            )

    def selecionar_aluno_lista(self, event=None):

        selecionado = self.aluno_listbox.curselection()

        if not selecionado:
            return

        valor = self.aluno_listbox.get(
            selecionado[0]
        )

        self.aluno_entry.delete(0, "end")

        self.aluno_entry.insert(
            0,
            valor
        )

        self.aluno_listbox.delete(0, "end")

        # salva aluno selecionado
        self.aluno_selecionado = valor

