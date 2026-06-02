# views/alunos_page.py

import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from database.database import SessionLocal
from models.aluno import Aluno


class AlunosPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.session = SessionLocal()

        self.aluno_selecionado_id = None

        self.configure(fg_color="transparent")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.criar_header()

        self.criar_formulario()

        self.criar_tabela()

        self.listar_alunos()

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
            text="Gerenciamento de Alunos",
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
            text="Cadastro",
            font=("Arial", 22, "bold")
        )

        titulo_form.pack(
            pady=(20, 20)
        )

        # =========================
        # Nome
        # =========================

        nome_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        nome_frame.pack(
            fill="x",
            padx=20,
            pady=(5, 10)
        )

        ctk.CTkLabel(
            nome_frame,
            text="Nome",
            width=80,
            anchor="w"
        ).pack(
            side="left"
        )

        self.nome_entry = ctk.CTkEntry(
            nome_frame
        )

        self.nome_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =========================
        # Turma
        # =========================

        turma_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        turma_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            turma_frame,
            text="Turma",
            width=80,
            anchor="w"
        ).pack(
            side="left"
        )

        self.turma_entry = ctk.CTkEntry(
            turma_frame
        )

        self.turma_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =========================
        # Matrícula
        # =========================

        matricula_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        matricula_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            matricula_frame,
            text="Matrícula",
            width=80,
            anchor="w"
        ).pack(
            side="left"
        )

        self.matricula_entry = ctk.CTkEntry(
            matricula_frame
        )

        self.matricula_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =========================
        # Telefone
        # =========================

        telefone_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        telefone_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            telefone_frame,
            text="Telefone",
            width=80,
            anchor="w"
        ).pack(
            side="left"
        )

        self.telefone_entry = ctk.CTkEntry(
            telefone_frame
        )

        self.telefone_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =========================
        # Status
        # =========================

        self.ativo_switch = ctk.CTkSwitch(
            form_frame,
            text="Aluno ativo"
        )

        self.ativo_switch.select()

        self.ativo_switch.pack(
            anchor="w",
            padx=20,
            pady=15
        )

        # =========================
        # Botões
        # =========================

        self.salvar_btn = ctk.CTkButton(
            form_frame,
            text="Salvar",
            height=40,
            command=self.salvar_aluno
        )

        self.salvar_btn.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        self.atualizar_btn = ctk.CTkButton(
            form_frame,
            text="Atualizar",
            height=40,
            fg_color="#d68c00",
            hover_color="#b57400",
            command=self.atualizar_aluno
        )

        self.atualizar_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.excluir_btn = ctk.CTkButton(
            form_frame,
            text="Excluir",
            height=40,
            fg_color="#c0392b",
            hover_color="#962d22",
            command=self.excluir_aluno
        )

        self.excluir_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )
        """
        self.limpar_btn = ctk.CTkButton(
            form_frame,
            text="Limpar",
            height=40,
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
            placeholder_text="Pesquisar aluno..."
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
            command=self.pesquisar_alunos
        )

        pesquisar_btn.pack(side="left")

        # Treeview

        colunas = (
            "id",
            "nome",
            "turma",
            "matricula",
            "telefone",
            "ativo"
        )

        self.tree = ttk.Treeview(
            tabela_frame,
            columns=colunas,
            show="headings",
            height=20
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("turma", text="Turma")
        self.tree.heading("matricula", text="Matrícula")
        self.tree.heading("telefone", text="Telefone")
        self.tree.heading("ativo", text="Ativo")

        self.tree.column("id", width=60)
        self.tree.column("nome", width=220)
        self.tree.column("turma", width=120)
        self.tree.column("matricula", width=120)
        self.tree.column("telefone", width=140)
        self.tree.column("ativo", width=80)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selecionar_aluno
        )

    # =========================================================
    # CRUD
    # =========================================================

    def salvar_aluno(self):

        nome = self.nome_entry.get()
        turma = self.turma_entry.get()
        matricula = self.matricula_entry.get().strip()
        telefone = self.telefone_entry.get()
        ativo = self.ativo_switch.get()

        if not nome or not turma:

            messagebox.showwarning(
                "Aviso",
                "Nome e turma são obrigatórios."
            )

            return

        aluno = Aluno(
            nome=nome,
            turma=turma,
            matricula=matricula or None,
            telefone=telefone,
            ativo=bool(ativo)
        )

        self.session.add(aluno)

        self.session.commit()

        self.listar_alunos()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Aluno cadastrado."
        )

    def listar_alunos(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        alunos = self.session.query(Aluno).all()

        for aluno in alunos:

            self.tree.insert(
                "",
                "end",
                values=(
                    aluno.id,
                    aluno.nome,
                    aluno.turma,
                    aluno.matricula if aluno.matricula != None else "",
                    aluno.telefone,
                    "Sim" if aluno.ativo else "Não"
                )
            )

    def selecionar_aluno(self, event):

        selecionado = self.tree.selection()

        if not selecionado:
            return

        dados = self.tree.item(selecionado[0])["values"]

        self.aluno_selecionado_id = dados[0]

        self.limpar_campos()

        self.nome_entry.insert(0, dados[1])
        self.turma_entry.insert(0, dados[2])
        self.matricula_entry.insert(0, dados[3])
        self.telefone_entry.insert(0, dados[4])

        if dados[5] == "Sim":
            self.ativo_switch.select()
        else:
            self.ativo_switch.deselect()

    def atualizar_aluno(self):

        if not self.aluno_selecionado_id:
            messagebox.showwarning(
            "Aviso",
            "Selecione um aluno."
        )
            return

        aluno = self.buscar_aluno()

        if not aluno:
            messagebox.showerror(
            "Erro",
            "Aluno não encontrado."
        )
            return

        self.preencher_dados_aluno(aluno)

        self.session.commit()

        self.listar_alunos()
        self.limpar_campos()

        messagebox.showinfo(
        "Sucesso",
        "Aluno atualizado."
        )
    def excluir_aluno(self):

        if not self.aluno_selecionado_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um aluno."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmação",
            "Deseja excluir este aluno?"
        )

        if not confirmar:
            return

        aluno = self.session.query(Aluno).filter_by(
            id=self.aluno_selecionado_id
        ).first()

        self.session.delete(aluno)

        self.session.commit()

        self.listar_alunos()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Aluno excluído."
        )

    def pesquisar_alunos(self):

        termo = self.pesquisa_entry.get()

        for item in self.tree.get_children():
            self.tree.delete(item)

        alunos = self.session.query(Aluno).filter(
            Aluno.nome.like(f"%{termo}%")
        ).all()

        for aluno in alunos:

            self.tree.insert(
                "",
                "end",
                values=(
                    aluno.id,
                    aluno.nome,
                    aluno.turma,
                    aluno.matricula,
                    aluno.telefone,
                    "Sim" if aluno.ativo else "Não"
                )
            )

    # =========================================================
    # UTILIDADES
    # =========================================================

    def limpar_campos(self):

        self.nome_entry.delete(0, "end")
        self.turma_entry.delete(0, "end")
        self.matricula_entry.delete(0, "end")
        self.telefone_entry.delete(0, "end")

        self.ativo_switch.select()

    def buscar_aluno(self):

        return self.session.query(Aluno).filter_by(
        id=self.aluno_selecionado_id
    ).first()

    def preencher_dados_aluno(self, aluno):

        aluno.nome = self.nome_entry.get()
        aluno.turma = self.turma_entry.get()
        aluno.matricula = self.matricula_entry.get()
        aluno.telefone = self.telefone_entry.get()
        aluno.ativo = bool(self.ativo_switch.get())