import tkinter as tk
from window import Window
from xwm_icons import ActionIcons
from xwm_db_query import XwmDbQuery


class ActionBar(tk.Frame):
    def __init__(self, master, ship_id=0, pack_side='top', grid_pos=None):
        tk.Frame.__init__(self, master, bg='black')
        if grid_pos:
            self.grid(row=grid_pos[0], column=grid_pos[1])
        else:
            self.pack(side=pack_side)

        self.current_ship_id = None

        self.action_icons = ActionIcons()

        self.header = tk.Label(self, bg='dim gray', text='Action Bar', font=('sans-serif', 16))
        self.header.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.action_slots = []
        for j in range(4):
            self.action_slots.append(tk.Label(self, bg='snow3', image=self.action_icons.get_icon('blank_icon'),
                                              text='', font=('sans-serif', 7), wraplength=60, width=60,
                                              compound='top'))
                                              # compound='none'))
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
    app = Window(root)
    ActionBar(app, shipId)
    root.mainloop()
