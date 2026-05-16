# views/pages/emprestimos_page.py

import customtkinter as ctk


class EmprestimosPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = ctk.CTkLabel(
            self,
            text="Empréstimos",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            pady=30
        )