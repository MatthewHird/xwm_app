import tkinter as tk
from tkinter import ttk
from global_environment import GlobalEnvironment
from ship_info import ShipInfo


class MainMenu(ttk.Frame):
    def __init__(self, master, pack_params=None, grid_params=None):
        ttk.Frame.__init__(self, master)

        self.options = GlobalEnvironment.get_stylesheet()
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.butt_frame = ttk.Frame(self)
        self.butt_frame.pack(side='top')
        self.prev_butt = ttk.Button(self.butt_frame, text='prev', command=self.prev_ship_info)
        self.prev_butt.pack(side='left')
        self.next_butt = ttk.Button(self.butt_frame, text='next', command=self.next_ship_info)
        self.next_butt.pack(side='right')

        self.ship_id = 1
        self.ship_info = ShipInfo(self, ship_id=self.ship_id, pack_params={'side': 'bottom'})

    def prev_ship_info(self):
        self.ship_id += -1
        if self.ship_id < 1:
            self.ship_id = 68
        self.ship_info.update_ship_info(self.ship_id)

    def next_ship_info(self):
        self.ship_id += 1
        if self.ship_id > 68:
            self.ship_id = 1
        self.ship_info.update_ship_info(self.ship_id)
