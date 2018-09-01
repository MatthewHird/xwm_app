import tkinter as tk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery


class PilotList(tk.Frame):
    def __init__(self, master, ship_id=0, pack_params=None, grid_params=None):
        tk.Frame.__init__(self, master, bg='black')
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
                color = 'wheat3'
                if i % 2 == 1:
                    color = 'wheat2'
                if i > 0 and j == 1:
                    self.pilot_table[i].append([])
                    self.pilot_table[i][j].append(tk.Frame(self, bg=color, relief='raised', bd=2, width=14))
                    self.pilot_table[i][j].append(tk.Label(self.pilot_table[i][j][0], bg=color, font=('sans-serif', 8),
                                                           width=2))
                    self.pilot_table[i][j][1].grid(row=0, column=0, sticky='ns')
                    self.pilot_table[i][j].append(tk.Label(self.pilot_table[i][j][0], bg=color, font=('sans-serif', 8),
                                                           wraplength='100p'))
                    self.pilot_table[i][j][2].grid(row=0, column=1, sticky='nsew')
                else:
                    self.pilot_table[i].append(tk.Label(self, bg=color, font=('sans-serif', 8), padx=5,
                                                        relief='raised', bd=2))

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
                    self.pilot_table[i][j][0].grid_forget()

                else:
                    self.pilot_table[i][j].grid_forget()

        k = 0
        for pilot in pilots_data:
            k += 1
            for j in range(4):
                if j == 0:
                    self.pilot_table[k][j].config(text=str(pilot['pilot_skill']))
                    self.pilot_table[k][j].grid(row=k, column=j, sticky='nsew')
                elif j == 1:
                    if pilot['unique_name_id'] != 0:
                        self.pilot_table[k][j][1].config(text='*')
                    else:
                        self.pilot_table[k][j][1].config(text='')
                    self.pilot_table[k][j][2].config(text=pilot['card_name'])
                    self.pilot_table[k][j][0].grid(row=k, column=j, sticky='nsew')
                elif j == 2:
                    if pilot['elite_upgrade']:
                        self.pilot_table[k][j].config(text='Yes')
                    else:
                        self.pilot_table[k][j].config(text='No')
                    self.pilot_table[k][j].grid(row=k, column=j, sticky='nsew')
                elif j == 3:
                    self.pilot_table[k][j].config(text=str(pilot['point_cost']))
                    self.pilot_table[k][j].grid(row=k, column=j, sticky='nsew')
            if k >= 15:
                break

    def __generate_header(self):
        self.pilot_table[0][0].config(text='PS')
        self.pilot_table[0][1].config(text='Pilot Name', wraplength='90p', width=14, anchor='w', padx=20)
        self.pilot_table[0][2].config(text='Elite?')
        self.pilot_table[0][3].config(text='Point Cost')
        for j in range(4):
            self.pilot_table[0][j].config(bg='wheat4', font=('sans-serif', 10))
            self.pilot_table[0][j].grid(row=0, column=j, sticky='nsew')


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    PilotList(app, shipId)
    root.mainloop()
