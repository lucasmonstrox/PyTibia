import tkinter as tk
from tkinter import messagebox, ttk


class InventoryPage(tk.Frame):
    backpacks = [
        '25 Years Backpack',
        'Anniversary Backpack',
        'Beach Backpack',
        'Birthday Backpack',
        'Brocade Backpack',
        'Buggy Backpack',
        'Cake Backpack',
        'Camouflage Backpack',
        'Crown Backpack',
        'Crystal Backpack',
        'Deepling Backpack',
        'Demon Backpack',
        'Dragon Backpack',
        'Expedition Backpack',
        'Fur Backpack',
        'Glooth Backpack',
        'Heart Backpack',
        'Minotaur Backpack',
        'Moon Backpack',
        'Mushroom Backpack',
        'Pannier Backpack',
        'Pirate Backpack',
        'Raccoon Backpack',
        'Santa Backpack',
        'Wolf Backpack',
    ]

    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
        self.mainBackpackFrame = tk.LabelFrame(
            self, text='Main Backpack', padx=10, pady=10)
        self.mainBackpackFrame.grid(column=0, row=0, padx=10,
                                    pady=10, sticky='nsew')

        self.mainBackpackFrame.rowconfigure(0, weight=1)
        self.mainBackpackFrame.columnconfigure(0, weight=1)

        self.listOfMainBackpacksCombobox = ttk.Combobox(
            self.mainBackpackFrame, values=self.backpacks, state='readonly')
        if self.context.enabledProfile is not None and self.context.enabledProfile['config']['backpacks']['main'] is not None:
            self.listOfMainBackpacksCombobox.set(
                self.context.enabledProfile['config']['backpacks']['main'])
        self.listOfMainBackpacksCombobox.grid(row=0, column=0, sticky='ew')
        self.listOfMainBackpacksCombobox.bind(
            "<<ComboboxSelected>>", self.setMainBackpack)

        self.lootBackpackFrame = tk.LabelFrame(
            self, text='Loot Backpack', padx=10, pady=10)
        self.lootBackpackFrame.grid(
            row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.lootBackpackFrame.rowconfigure(0, weight=1)
        self.lootBackpackFrame.columnconfigure(0, weight=1)

        self.listOfLootBackpacksombobox = ttk.Combobox(
            self.lootBackpackFrame, values=self.backpacks, state='readonly')
        if self.context.enabledProfile is not None and self.context.enabledProfile['config']['backpacks']['loot'] is not None:
            self.listOfLootBackpacksombobox.set(
                self.context.enabledProfile['config']['backpacks']['loot'])
        self.listOfLootBackpacksombobox.grid(row=0, column=0, sticky='ew')
        self.listOfLootBackpacksombobox.bind(
            "<<ComboboxSelected>>", self.setLootBackpack)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

    def setMainBackpack(self, _):
        if not self.canChangeBackpack():
            self.listOfMainBackpacksCombobox.set(
                self.context.enabledProfile['config']['backpacks']['main'])
            messagebox.showerror(
                'Erro', 'The Main Backpack has to be different from the Loot Backpack!')
            return
        self.context.updateMainBackpack(self.listOfMainBackpacksCombobox.get())

    def setLootBackpack(self, _):
        if not self.canChangeBackpack():
            self.listOfLootBackpacksombobox.set(
                self.context.enabledProfile['config']['backpacks']['loot'])
            messagebox.showerror(
                'Erro', 'The Loot Backpack has to be different from the Main Backpack!')
            return
        self.context.updateLootBackpack(self.listOfLootBackpacksombobox.get())

    def canChangeBackpack(self):
        return self.listOfMainBackpacksCombobox.get(
        ) != self.listOfLootBackpacksombobox.get()
