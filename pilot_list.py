import tkinter as tk
from tkinter import ttk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery
from global_environment import GlobalEnvironment


class PilotList(ttk.Frame):
    def __init__(self, master, ship_id=0, pack_params=None, grid_params=None):
        ttk.Frame.__init__(self, master)

        self.options = GlobalEnvironment.get_stylesheet()
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.current_ship_id = None

        self.pilot_table = []

        for i in range(15):
            self.pilot_table.append([])
            for j in range(4):
                if i == 0:
                    if j == 1:
                        self.pilot_table[i].append(
                            ttk.Label(self, style='PilotName.Header.Regular.PilotList.TLabel'))
                    else:
                        self.pilot_table[i].append(ttk.Label(self, style='Header.Regular.PilotList.TLabel'))
                elif i > 0 and j == 1:
                    self.pilot_table[i].append([])
                    if i % 2 == 1:
                        self.pilot_table[i][j].append(
                            ttk.Frame(self, style='Odd.PilotList.TFrame', **self.options['p_name_frame.pilot_list']))
                        self.pilot_table[i][j].append(
                            ttk.Label(self.pilot_table[i][j][0], style='Unique.PilotList.TLabel',
                                      **self.options['odd.pilot_list']))
                        self.pilot_table[i][j].append(
                            ttk.Label(self.pilot_table[i][j][0], style='PilotName.PilotList.TLabel',
                                      **self.options['odd.pilot_list']))
                    else:
                        self.pilot_table[i][j].append(
                            ttk.Frame(self, style='Even.PilotList.TFrame',
                                      **self.options['p_name_frame.pilot_list']))
                        self.pilot_table[i][j].append(
                            ttk.Label(self.pilot_table[i][j][0], style='Unique.PilotList.TLabel',
                                      **self.options['even.pilot_list']))
                        self.pilot_table[i][j].append(
                            ttk.Label(self.pilot_table[i][j][0], style='PilotName.PilotList.TLabel',
                                      **self.options['even.pilot_list']))

                    self.pilot_table[i][j][1].grid(row=0, column=0, sticky='ns')
                    self.pilot_table[i][j][2].grid(row=0, column=1, sticky='nsew')
                else:
                    if i % 2 == 1:
                        self.pilot_table[i].append(ttk.Label(self, style='Regular.PilotList.TLabel',
                                                             **self.options['odd.pilot_list']))
                    else:
                        self.pilot_table[i].append(ttk.Label(self, style='Regular.PilotList.TLabel',
                                                             **self.options['even.pilot_list']))

                if i > 0 and j == 1:
                    self.pilot_table[i][j][0].grid(row=i, column=j, sticky='nsew')
                else:
                    self.pilot_table[i][j].grid(row=i, column=j, sticky='nsew')

        self.__generate_header()
        self.update_pilot_list(ship_id=ship_id)

    def update_pilot_list(self, ship_id=0):
        if ship_id == self.current_ship_id:
            return True
        self.current_ship_id = ship_id

        pilots_data = XwmDbQuery.get_pilot_list_data(ship_id)
        if not pilots_data:
            return False

        for i in range(1, 15):
            for j in range(4):
                if j == 1:
                    self.pilot_table[i][j][0].grid_remove()

                else:
                    self.pilot_table[i][j].grid_remove()

        k = 0
        for pilot in pilots_data:
            k += 1
            for j in range(4):
                if j == 0:
                    self.pilot_table[k][j].config(text=str(pilot['pilot_skill']))
                    self.pilot_table[k][j].grid()
                elif j == 1:
                    if pilot['unique_name_id'] != 0:
                        self.pilot_table[k][j][1].config(text='*')
                    else:
                        self.pilot_table[k][j][1].config(text='')

                    pilot_name = pilot['card_name']
                    if pilot['variant']:
                        pilot_name += ' (' + pilot['variant'] + ')'
                    self.pilot_table[k][j][2].config(text=pilot_name)
                    self.pilot_table[k][j][0].grid()
                elif j == 2:
                    if pilot['elite_upgrade']:
                        self.pilot_table[k][j].config(text='Yes')
                    else:
                        self.pilot_table[k][j].config(text='No')
                    self.pilot_table[k][j].grid()
                elif j == 3:
                    self.pilot_table[k][j].config(text=str(pilot['point_cost']))
                    self.pilot_table[k][j].grid()
            if k >= 15:
                break

    def __generate_header(self):
        self.pilot_table[0][0].config(text='PS')
        self.pilot_table[0][1].config(text='     Pilot Name')
        self.pilot_table[0][2].config(text='Elite?')
        self.pilot_table[0][3].config(text='Point Cost')


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    PilotList(app, shipId)
    root.mainloop()
