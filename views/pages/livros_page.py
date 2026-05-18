# views/livros_page.py

import customtkinter as ctk

from tkinter import ttk
from tkinter import messagebox

from database.database import SessionLocal

from models.livro import Livro


class LivrosPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.session = SessionLocal()

        self.livro_selecionado_id = None

        self.configure(fg_color="transparent")

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(1, weight=1)

        self.criar_header()

        self.criar_formulario()

        self.criar_tabela()

        self.listar_livros()

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
            text="Gerenciamento de Livros",
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

        # =====================================================
        # Obra
        # =====================================================

        obra_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        obra_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            obra_frame,
            text="Obra",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.obra_entry = ctk.CTkEntry(
            obra_frame
        )

        self.obra_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Autor
        # =====================================================

        autor_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        autor_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            autor_frame,
            text="Autor",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.autor_entry = ctk.CTkEntry(
            autor_frame
        )

        self.autor_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Ano
        # =====================================================

        ano_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        ano_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            ano_frame,
            text="Ano",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.ano_entry = ctk.CTkEntry(
            ano_frame
        )

        self.ano_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Categoria
        # =====================================================

        categoria_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        categoria_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            categoria_frame,
            text="Categoria",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.categoria_entry = ctk.CTkEntry(
            categoria_frame
        )

        self.categoria_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Editora
        # =====================================================

        editora_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        editora_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            editora_frame,
            text="Editora",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.editora_entry = ctk.CTkEntry(
            editora_frame
        )

        self.editora_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Quantidade
        # =====================================================

        quantidade_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        quantidade_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            quantidade_frame,
            text="Quantidade",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.quantidade_entry = ctk.CTkEntry(
            quantidade_frame
        )

        self.quantidade_entry.insert(0, "1")

        self.quantidade_entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Observação
        # =====================================================

        observacao_label = ctk.CTkLabel(
            form_frame,
            text="Observação"
        )

        observacao_label.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.observacao_textbox = ctk.CTkTextbox(
            form_frame,
            height=100
        )

        self.observacao_textbox.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        # =====================================================
        # Status
        # =====================================================

        status_frame = ctk.CTkFrame(
            form_frame,
            fg_color="transparent"
        )

        status_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            status_frame,
            text="Status",
            width=90,
            anchor="w"
        ).pack(
            side="left"
        )

        self.status_combobox = ctk.CTkComboBox(
            status_frame,
            values=[
                "disponivel",
                "indisponivel"
            ]
        )

        self.status_combobox.set(
            "disponivel"
        )

        self.status_combobox.pack(
            side="left",
            fill="x",
            expand=True
        )

        # =====================================================
        # Botões
        # =====================================================

        self.salvar_btn = ctk.CTkButton(
            form_frame,
            text="Salvar",
            height=42,
            command=self.salvar_livro
        )

        self.salvar_btn.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        self.atualizar_btn = ctk.CTkButton(
            form_frame,
            text="Atualizar",
            height=42,
            fg_color="#d68c00",
            hover_color="#b57400",
            command=self.atualizar_livro
        )

        self.atualizar_btn.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.excluir_btn = ctk.CTkButton(
            form_frame,
            text="Excluir",
            height=42,
            fg_color="#c0392b",
            hover_color="#962d22",
            command=self.excluir_livro
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
            placeholder_text="Pesquisar livro..."
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
            command=self.pesquisar_livros
        )

        pesquisar_btn.pack(side="left")

        # Treeview

        colunas = (
            "id",
            "obra",
            "autor",
            "ano",
            "categoria",
            "editora",
            "quantidade",
            "status"
        )

        self.tree = ttk.Treeview(
            tabela_frame,
            columns=colunas,
            show="headings",
            height=20
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("obra", text="Obra")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("ano", text="Ano")
        self.tree.heading("categoria", text="Categoria")
        self.tree.heading("editora", text="Editora")
        self.tree.heading("quantidade", text="Qtd")
        self.tree.heading("status", text="Status")

        self.tree.column("id", width=60)
        self.tree.column("obra", width=250)
        self.tree.column("autor", width=180)
        self.tree.column("ano", width=80)
        self.tree.column("categoria", width=120)
        self.tree.column("editora", width=140)
        self.tree.column("quantidade", width=70)
        self.tree.column("status", width=120)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selecionar_livro
        )

    # =========================================================
    # CRUD
    # =========================================================

    def salvar_livro(self):

        obra = self.obra_entry.get()
        autor = self.autor_entry.get()

        if not obra or not autor:

            messagebox.showwarning(
                "Aviso",
                "Obra e autor são obrigatórios."
            )

            return

        try:
            ano = int(self.ano_entry.get()) \
                if self.ano_entry.get() else None

            quantidade = int(
                self.quantidade_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Ano e quantidade devem ser numéricos."
            )

            return

        livro = Livro(
            obra=obra,
            autor=autor,
            ano=ano,
            categoria=self.categoria_entry.get(),
            editora=self.editora_entry.get(),
            quantidade=quantidade,
            observacao=self.observacao_textbox.get(
                "1.0",
                "end"
            ).strip(),
            status=self.status_combobox.get()
        )

        self.session.add(livro)

        self.session.commit()

        self.listar_livros()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Livro cadastrado."
        )

    def listar_livros(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        livros = self.session.query(
            Livro
        ).all()

        for livro in livros:

            self.tree.insert(
                "",
                "end",
                values=(
                    livro.id,
                    livro.obra,
                    livro.autor,
                    livro.ano,
                    livro.categoria,
                    livro.editora,
                    livro.quantidade,
                    livro.status
                )
            )

    def selecionar_livro(self, event):

        selecionado = self.tree.selection()

        if not selecionado:
            return

        dados = self.tree.item(
            selecionado[0]
        )["values"]

        self.livro_selecionado_id = dados[0]

        livro = self.session.query(
            Livro
        ).filter_by(
            id=self.livro_selecionado_id
        ).first()

        self.limpar_campos()

        self.obra_entry.insert(0, livro.obra)
        self.autor_entry.insert(0, livro.autor)

        if livro.ano:
            self.ano_entry.insert(0, livro.ano)

        if livro.categoria:
            self.categoria_entry.insert(
                0,
                livro.categoria
            )

        if livro.editora:
            self.editora_entry.insert(
                0,
                livro.editora
            )

        
        self.quantidade_entry.delete(0, "end")
        self.quantidade_entry.insert(
            0,
            livro.quantidade
        )

        if livro.observacao:

            self.observacao_textbox.insert(
                "1.0",
                livro.observacao
            )

        self.status_combobox.set(
            livro.status
        )

    def atualizar_livro(self):

        if not self.livro_selecionado_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um livro."
            )

            return

        livro = self.session.query(
            Livro
        ).filter_by(
            id=self.livro_selecionado_id
        ).first()

        try:
            livro.ano = int(
                self.ano_entry.get()
            ) if self.ano_entry.get() else None

            livro.quantidade = int(
                self.quantidade_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Ano e quantidade devem ser numéricos."
            )

            return

        livro.obra = self.obra_entry.get()

        livro.autor = self.autor_entry.get()

        livro.categoria = self.categoria_entry.get()

        livro.editora = self.editora_entry.get()

        livro.observacao = self.observacao_textbox.get(
            "1.0",
            "end"
        ).strip()

        livro.status = self.status_combobox.get()

        self.session.commit()

        self.listar_livros()

        self.limpar_campos()
        self.limpar_selecao()

        messagebox.showinfo(
    "Sucesso",
    "Livro atualizado."
)
    def excluir_livro(self):

        if not self.livro_selecionado_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um livro."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmação",
            "Deseja excluir este livro?"
        )

        if not confirmar:
            return

        livro = self.session.query(
            Livro
        ).filter_by(
            id=self.livro_selecionado_id
        ).first()

        self.session.delete(livro)

        self.session.commit()

        self.listar_livros()

        self.listar_livros()

        self.limpar_campos()
        self.limpar_selecao()

        messagebox.showinfo(
            "Sucesso",
            "Livro excluído."
        )

    def pesquisar_livros(self):

        termo = self.pesquisa_entry.get()

        for item in self.tree.get_children():
            self.tree.delete(item)

        livros = self.session.query(
            Livro
        ).filter(
            Livro.obra.like(f"%{termo}%")
        ).all()

        for livro in livros:

            self.tree.insert(
                "",
                "end",
                values=(
                    livro.id,
                    livro.obra,
                    livro.autor,
                    livro.ano,
                    livro.categoria,
                    livro.editora,
                    livro.quantidade,
                    livro.status
                )
            )

    # =========================================================
    # UTILIDADES
    # =========================================================

    def limpar_campos(self):

        self.obra_entry.delete(0, "end")

        self.autor_entry.delete(0, "end")

        self.ano_entry.delete(0, "end")

        self.categoria_entry.delete(0, "end")

        self.editora_entry.delete(0, "end")

        self.quantidade_entry.delete(0, "end")


        self.observacao_textbox.delete(
            "1.0",
            "end"
        )

        self.status_combobox.set(
            "disponivel"
        )
    def limpar_selecao(self):

        self.livro_selecionado_id = None