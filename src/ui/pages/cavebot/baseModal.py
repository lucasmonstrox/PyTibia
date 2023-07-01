import tkinter as tk
from tkinter import messagebox


class BaseModal(tk.Toplevel):
    def __init__(self, parent, waypoint=None, onConfirm=lambda: {}):
        super().__init__(parent)
        self.resizable(False, False)
        self.title('Configure waypoint')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.onConfirm = onConfirm

        self.frame = tk.LabelFrame(
            self, text='Label:', padx=10, pady=10)
        self.frame.grid(column=0, row=0, columnspan=2, padx=10,
                        pady=10, sticky='nsew')
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.labelEntry = tk.Entry(self.frame)
        self.labelEntry.grid(
            row=1, column=0, sticky='nsew')
        if waypoint is not None and waypoint['label']:
            self.labelEntry.insert(0, waypoint['label'])

        self.confirmButton = tk.Button(
            self, text='Confirm', command=self.confirm)
        self.confirmButton.grid(
            row=6, column=0, padx=(10, 5), pady=(5, 10), sticky='nsew')

        self.cancelButton = tk.Button(
            self, text='Cancel', command=self.destroy)
        self.cancelButton.grid(
            row=6, column=1, padx=(5, 10), pady=(5, 10), sticky='nsew')

    def confirm(self):
        self.onConfirm(self.labelEntry.get(), {})
        self.destroy()
