# views/sidebar.py

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, change_page_callback):
        super().__init__(
            parent,
            width=220,
            corner_radius=0
        )

        self.grid_rowconfigure(10, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Biblioteca",
            font=("Arial", 24, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(30, 20)
        )

        botoes = [
            ("Dashboard", "dashboard"),
            ("Livros", "livros"),
            ("Alunos", "alunos"),
            ("Empréstimos", "emprestimos"),
        ]

        for index, (texto, pagina) in enumerate(botoes, start=1):

            botao = ctk.CTkButton(
                self,
                text=texto,
                height=40,
                command=lambda p=pagina:
                    change_page_callback(p)
            )

            botao.grid(
                row=index,
                column=0,
                padx=20,
                pady=10,
                sticky="ew"
            )