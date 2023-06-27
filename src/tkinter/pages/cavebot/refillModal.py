import tkinter as tk
from tkinter import messagebox, ttk


class RefillModal(tk.Toplevel):
    def __init__(self, parent, onConfirm=lambda: {}):
        super().__init__(parent)
        self.resizable(False, False)
        self.title('Configure potions for refill')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.onConfirm = onConfirm

        self.healthPotionFrame = tk.LabelFrame(
            self, text='Health Potion', padx=10, pady=10)
        self.healthPotionFrame.grid(column=0, row=0, padx=(10, 5),
                                    pady=(10, 0), sticky='nsew')
        self.healthPotionFrame.rowconfigure(0, weight=1)
        self.healthPotionFrame.rowconfigure(1, weight=1)

        self.healthPotionCombobox = ttk.Combobox(
            self.healthPotionFrame, values=['Small Health Potion', 'Health Potion', 'Strong Health Potion', 'Great Health Potion', 'Ultimate Health Potion', 'Supreme Health Potion'], state='readonly')
        self.healthPotionCombobox.grid(
            row=0, column=0, sticky='nsew')

        self.healthPotionEntry = tk.Entry(self.healthPotionFrame, validate='key',
                                          validatecommand=(self.register(self.validateNumber), "%P"))
        self.healthPotionEntry.grid(
            row=1, column=0, sticky='nsew', pady=(10, 0))

        self.manaPotionFrame = tk.LabelFrame(
            self, text='Mana Potion', padx=10, pady=10)
        self.manaPotionFrame.grid(column=1, row=0, padx=(5, 10),
                                  pady=(10, 0), sticky='nsew')
        self.manaPotionFrame.rowconfigure(0, weight=1)
        self.manaPotionFrame.rowconfigure(1, weight=1)

        self.manaPotionCombobox = ttk.Combobox(
            self.manaPotionFrame, values=['Mana Potion', 'Strong Mana Potion', 'Great Mana Potion', 'Ultimate Mana Potion'], state='readonly')
        self.manaPotionCombobox.grid(
            row=0, column=0, sticky='nsew')

        self.manaPotionEntry = tk.Entry(self.manaPotionFrame, validate='key',
                                        validatecommand=(self.register(self.validateNumber), "%P"))
        self.manaPotionEntry.grid(
            row=1, column=0, sticky='nsew', pady=(10, 0))

        self.confirmButton = tk.Button(
            self, text='Confirm', command=self.confirm)
        self.confirmButton.grid(
            row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.cancelButton = tk.Button(
            self, text='Cancel', command=self.destroy)
        self.cancelButton.grid(
            row=1, column=1, padx=10, pady=10, sticky='nsew')

    def validateNumber(self, value: int) -> bool:
        if value.isdigit() and int(value) > 0:
            return True
        messagebox.showerror(
            'Error', "Digite um número válido maior que zero.")
        return False

    def confirm(self):
        self.onConfirm({
            'healthPotion': {
                'item': self.healthPotionCombobox.get(),
                'quantity': self.healthPotionEntry.get()
            },
            'manaPotion': {
                'item': self.manaPotionCombobox.get(),
                'quantity': self.manaPotionEntry.get()
            },
        })
        self.destroy()
