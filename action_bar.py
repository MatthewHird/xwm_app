import tkinter as tk
from tkinter import ttk
from app_window import AppWindow
from xwm_icons import ActionIcons
from xwm_db_query import XwmDbQuery
from global_environment import GlobalEnvironment


class ActionBar(ttk.Frame):
    def __init__(self, master, ship_id=0, pack_params=None, grid_params=None):
        ttk.Frame.__init__(self, master, style='ActionBar.TFrame')

        self.options = GlobalEnvironment.get_stylesheet()
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.current_ship_id = None

        self.action_icons = ActionIcons()

        self.header = ttk.Label(self, style='Header.ActionBar.TLabel', text='Action Bar',
                                **self.options['header.action_bar'])
        self.header.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.action_slots = []
        for j in range(4):
            self.action_slots.append(ttk.Label(self, style='Slot.ActionBar.TLabel', text='',
                                               image=self.action_icons.get_icon('blank_icon'),
                                               **self.options['slot.action_bar']))

            self.action_slots[j].grid(row=1, column=j, sticky='nsew')

        self.update_action_bar(ship_id)

    def update_action_bar(self, ship_id=0):
        if ship_id == self.current_ship_id:
            return True
        self.current_ship_id = ship_id

        action_data = XwmDbQuery.get_action_bar(ship_id)
        if not action_data:
            return False

        for j in range(4):
            self.action_slots[j].config(image=self.action_icons.get_icon('blank_icon'), text=' ')

        for index, action in enumerate(action_data):
            self.action_slots[index].config(image=self.action_icons.get_icon(action['action_name'] + '_black'),
                                            text=action['print_name'])


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    ActionBar(app, shipId)
    root.mainloop()
