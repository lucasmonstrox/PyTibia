import tkinter as tk


class SpellsTab(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
