import tkinter as tk
from app_window import AppWindow
from xwm_icons import UpgradeIcons
from xwm_db_query import XwmDbQuery


class UpgradeBar(tk.Frame):
    def __init__(self, master, ship_id=0, pack_params=None, grid_params=None):
        tk.Frame.__init__(self, master, bg='black', bd=2)
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.current_ship_id = None

        self.upgrade_icons = UpgradeIcons()

        self.header = tk.Label(self, bg='dim gray', text='Upgrade Bar', font=('sans-serif', 16))
        self.header.grid(row=0, column=0, columnspan=7, sticky='nsew')

        self.upgrade_slots = []
        for j in range(7):
            self.upgrade_slots.append(tk.Label(self, bg='snow3', image=self.upgrade_icons.get_icon('blank_icon'),
                                               text='', font=('sans-serif', 7), wraplength=34, width=34,
                                               # compound='top'))
                                               compound='none'))
            self.upgrade_slots[j].grid(row=1, column=j, sticky='nsew')

        self.update_upgrade_bar(ship_id)

    def update_upgrade_bar(self, ship_id=0):
        if ship_id == self.current_ship_id:
            return True
        self.current_ship_id = ship_id

        upgrade_data = XwmDbQuery.get_upgrade_bar(ship_id)
        if not upgrade_data:
            return False

        for j in range(7):
            self.upgrade_slots[j].config(image=self.upgrade_icons.get_icon('blank_icon'), text=' ')

        for index, upgrade in enumerate(upgrade_data):
            self.upgrade_slots[index].config(image=self.upgrade_icons.get_icon(upgrade['upgrade_name'] + '_black'),
                                             text=upgrade['print_name'])


if __name__ == '__main__':
    shipId = 23
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    UpgradeBar(app, shipId)
    root.mainloop()