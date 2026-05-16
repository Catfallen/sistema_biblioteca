# views/pages/dashboard_page.py

import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            pady=30
        )