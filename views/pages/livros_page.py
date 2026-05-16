# views/pages/livros_page.py

import customtkinter as ctk


class LivrosPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = ctk.CTkLabel(
            self,
            text="Livros",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            pady=30
        )