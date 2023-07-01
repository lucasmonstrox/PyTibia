import tkinter as tk
from tkinter import messagebox


class RefillCheckerModal(tk.Toplevel):
    def __init__(self, parent, onConfirm=lambda: {}, waypoint=None):
        super().__init__(parent)
        self.resizable(False, False)
        self.title('Configure checker for refill')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.onConfirm = onConfirm

        self.labelEntry = tk.Entry(self)
        self.labelEntry.grid(
            row=0, column=0, columnspan=2, sticky='nsew')
        if waypoint is not None:
            self.labelEntry.insert(
                0, waypoint['options'].get('waypointLabelToRedirect'))

        self.frame = tk.LabelFrame(
            self, text='Minimum of:', padx=10, pady=10)
        self.frame.grid(column=0, row=1, columnspan=2, padx=10,
                        pady=10, sticky='nsew')
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.minimumOfHealthPotionLabel = tk.Label(
            self.frame, text='Health Potion:', anchor='w')
        self.minimumOfHealthPotionLabel.grid(
            row=0, column=0, sticky='nsew')

        self.minimumAmountOfHealthPotionsEntry = tk.Entry(self.frame, validate='key',
                                                          validatecommand=(self.register(self.validateNumber), "%P"))
        self.minimumAmountOfHealthPotionsEntry.grid(
            row=1, column=0, sticky='nsew')
        if waypoint is not None:
            self.minimumAmountOfHealthPotionsEntry.insert(
                0, waypoint['options'].get('minimumAmountOfHealthPotions'))

        self.minimumOfManaPotionLabel = tk.Label(
            self.frame, text='Mana Potion:', anchor='w')
        self.minimumOfManaPotionLabel.grid(
            row=2, column=0, sticky='nsew')

        self.minimumAmountOfManaPotionsEntry = tk.Entry(self.frame, validate='key',
                                                        validatecommand=(self.register(self.validateNumber), "%P"))
        self.minimumAmountOfManaPotionsEntry.grid(
            row=3, column=0, sticky='nsew')
        if waypoint is not None:
            self.minimumAmountOfManaPotionsEntry.insert(
                0, waypoint['options'].get('minimumAmountOfManaPotions'))

        self.minimumOfCapLabel = tk.Label(
            self.frame, text='Cap:', anchor='w')
        self.minimumOfCapLabel.grid(
            row=4, column=0, sticky='nsew')

        self.minimumAmountOfCapEntry = tk.Entry(self.frame, validate='key',
                                                validatecommand=(self.register(self.validateNumber), "%P"))
        self.minimumAmountOfCapEntry.grid(
            row=5, column=0, sticky='nsew')
        if waypoint is not None:
            self.minimumAmountOfCapEntry.insert(
                0, waypoint['options'].get('minimumAmountOfCap'))

        self.confirmButton = tk.Button(
            self, text='Confirm', command=self.confirm)
        self.confirmButton.grid(
            row=6, column=0, padx=(10, 5), pady=(5, 10), sticky='nsew')

        self.cancelButton = tk.Button(
            self, text='Cancel', command=self.destroy)
        self.cancelButton.grid(
            row=6, column=1, padx=(5, 10), pady=(5, 10), sticky='nsew')

    def validateNumber(self, value: int) -> bool:
        if value.isdigit() and int(value) > 0:
            return True
        messagebox.showerror(
            'Error', "Digite um número válido maior que zero.")
        return False

    def confirm(self):
        self.onConfirm(None, {
            'minimumAmountOfHealthPotions': self.minimumAmountOfHealthPotionsEntry.get(),
            'minimumAmountOfManaPotions': self.minimumAmountOfManaPotionsEntry.get(),
            'minimumAmountOfCap': self.minimumAmountOfCapEntry.get(),
            'waypointLabelToRedirect': self.labelEntry.get(),
        })
        self.destroy()
