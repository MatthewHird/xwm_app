import tkinter as tk
from tkinter import ttk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery
from global_environment import GlobalEnvironment


class ShipStats(ttk.Frame):
    def __init__(self, master, ship_id=0, pack_params=None, grid_params=None):
        ttk.Frame.__init__(self, master, style='ShipStats.TFrame')

        self.options = GlobalEnvironment.get_stylesheet()
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.current_ship_id = None

        self.headers = self.__generate_headers()
        self.ship_stats = []
        for i in range(4):
            self.ship_stats.append(ttk.Label(self, style='ShipStats.TLabel'))
            self.ship_stats[i].grid(row=(i+1), column=1, sticky='nsew')
        self.ship_stats[0].config(**self.options['attack.ship_stats'])
        self.ship_stats[1].config(**self.options['agility.ship_stats'])
        self.ship_stats[2].config(**self.options['hull.ship_stats'])
        self.ship_stats[3].config(**self.options['shield.ship_stats'])

        self.update_ship_stats(ship_id)

    def update_ship_stats(self, ship_id=0):
        if ship_id == self.current_ship_id:
            return True
        self.current_ship_id = ship_id

        ship_stats_data = XwmDbQuery.get_ship_stats(ship_id)
        if not ship_stats_data:
            return False

        if ship_stats_data['attack_or_energy'] == 'A':
            self.headers[1].config(text='Attack Value', **self.options['attack.ship_stats'])
            self.ship_stats[0].config(text=str(ship_stats_data['attack_energy_value']),
                                      **self.options['attack.ship_stats'])
        elif ship_stats_data['attack_or_energy'] == 'E':
            self.headers[1].config(text='Energy Value', **self.options['energy.ship_stats'])
            self.ship_stats[0].config(text=str(ship_stats_data['attack_energy_value']),
                                      **self.options['energy.ship_stats'])

        self.ship_stats[1].config(text=str(ship_stats_data['agility_value']))
        self.ship_stats[2].config(text=str(ship_stats_data['hull_value']))
        self.ship_stats[3].config(text=str(ship_stats_data['shield_value']))

    def __generate_headers(self):
        headers = []
        for i in range(5):
            if i == 0:
                headers.append(ttk.Label(self, style='Header.ShipStats.TLabel'))
                headers[i].grid(row=i, column=0, columnspan=2)
            else:
                headers.append(ttk.Label(self, style='ShipStats.TLabel'))
                headers[i].grid(row=i, column=0, sticky='nsew')

        headers[0].config(text='Ship Stats')
        headers[1].config(text='Attack Value', **self.options['attack.ship_stats'])
        headers[2].config(text='Agility Value', **self.options['agility.ship_stats'])
        headers[3].config(text='Hull Value', **self.options['hull.ship_stats'])
        headers[4].config(text='Shield Value', **self.options['shield.ship_stats'])

        return headers


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    ShipStats(app, shipId)
    root.mainloop()
