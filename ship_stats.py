import tkinter as tk
from window import Window
from xwm_db_query import XwmDbQuery


class ShipStats(tk.Frame):
    def __init__(self, master, ship_id=0, pack_side='top', grid_pos=None):
        tk.Frame.__init__(self, master, bg='black')
        if grid_pos:
            self.grid(row=grid_pos[0], column=grid_pos[1])
        else:
            self.pack(side=pack_side)

        self.current_ship_id = None

        self.update_ship_stats(ship_id)

    def update_ship_stats(self, ship_id=0):
        pass
