# views/main_window.py

import customtkinter as ctk

from views.sidebar import Sidebar

from views.pages.dashboard_page import DashboardPage
from views.pages.livros_page import LivrosPage
from views.pages.alunos_page import AlunosPage
from views.pages.emprestimos_page import EmprestimosPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema Biblioteca")

        self.geometry("1366x720")

        self.minsize(1000, 600)

        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(
            self,
            self.change_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.container = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.container.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.pages = {}

        self.create_pages()

        self.change_page("dashboard")

    def create_pages(self):

        self.pages["dashboard"] = DashboardPage(
            self.container
        )

        self.pages["livros"] = LivrosPage(
            self.container
        )

        self.pages["alunos"] = AlunosPage(
            self.container
        )

        self.pages["emprestimos"] = EmprestimosPage(
            self.container
        )

    def change_page(self, page_name):

        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(
            fill="both",
            expand=True
        )