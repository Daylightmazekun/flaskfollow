import tkinter as tk
from tkinter import messagebox as mes
from tkinter.ttk import Notebook

import requests

class ReadMarkdown(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ReadMarkdown file to mongodb")
        self.geometry("500x300")

        self.menu = tk.Menu(self, bg = "lightgrey", fg = "black")

