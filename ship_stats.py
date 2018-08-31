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

        self.headers = self.__generate_headers()
        self.ship_stats = []
        for i in range(4):
            self.ship_stats.append(tk.Label(self, bg='snow3', font=('sans-serif', 10)))
            self.ship_stats[i].grid(row=(i+1), column=1, sticky='nsew')
        self.ship_stats[0].config(fg='red')
        self.ship_stats[1].config(fg='green')
        self.ship_stats[2].config(fg='yellow')
        self.ship_stats[3].config(fg='blue')

        self.update_ship_stats(ship_id)

    def update_ship_stats(self, ship_id=0):
        if ship_id == self.current_ship_id:
            return True
        self.current_ship_id = ship_id

        ship_stats_data = XwmDbQuery.get_ship_stats(ship_id)
        if not ship_stats_data:
            return False

        if ship_stats_data['attack_or_energy'] == 'A':
            self.headers[1].config(text='Attack Value', fg='red')
            self.ship_stats[0].config(text=str(ship_stats_data['attack_energy_value']), fg='red')
        elif ship_stats_data['attack_or_energy'] == 'E':
            self.headers[1].config(text='Energy Value', fg='#202020')
            self.ship_stats[0].config(text=str(ship_stats_data['attack_energy_value']), fg='#202020')

        self.ship_stats[1].config(text=str(ship_stats_data['agility_value']))
        self.ship_stats[2].config(text=str(ship_stats_data['hull_value']))
        self.ship_stats[3].config(text=str(ship_stats_data['shield_value']))

    def __generate_headers(self):
        headers = []
        for i in range(5):
            headers.append(tk.Label(self, bg='snow3', font=('sans-serif', 10)))
            if i == 0:
                headers[i].grid(row=i, column=0, columnspan=2)
            else:
                headers[i].grid(row=i, column=0, sticky='nsew')

        headers[0].config(text='Ship Stats', bg='black', fg='white', font=('sans-serif', 16))
        headers[1].config(text='Attack Value', fg='red')
        headers[2].config(text='Agility Value', fg='green')
        headers[3].config(text='Hull Value', fg='yellow')
        headers[4].config(text='Shield Value', fg='blue')

        return headers


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = Window(root)
    ShipStats(app, shipId)
    root.mainloop()
