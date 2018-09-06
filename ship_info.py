import tkinter as tk
from tkinter import ttk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery
from ship_stats import ShipStats
from action_bar import ActionBar
from upgrade_bar import UpgradeBar
from pilot_list import PilotList
from maneuver_dial import ManeuverDial
from global_environment import GlobalEnvironment


class ShipInfo(ttk.Frame):
    def __init__(self, master, ship_name='', ship_id=0, pack_params=None, grid_params=None):
        ttk.Frame.__init__(self, master)

        self.options = GlobalEnvironment.get_stylesheet()
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.ship_name = ship_name
        self.ship_id = ship_id

        self.headers = []
        self.fields = []
        self.basic_info_frame = ttk.Frame(self)
        self.basic_info_frame.pack(side='top')

        self.__generate_headers_and_fields()

        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(side='bottom')

        # generate blank ship_stats
        self.ship_stats = ShipStats(self.bottom_frame, self.ship_id,
                                    grid_params={'row': 0, 'column': 0, 'sticky': 'n'})
        # generate blank action_bar
        self.action_bar = ActionBar(self.bottom_frame, self.ship_id,
                                    grid_params={'row': 1, 'column': 0})
        # generate blank upgrade_bar
        self.upgrade_bar = UpgradeBar(self.bottom_frame, self.ship_id,
                                      grid_params={'row': 2, 'column': 0})
        # generate empty maneuver_dial
        self.maneuver_dial = ManeuverDial(self.bottom_frame, self.ship_id,
                                          grid_params={'row': 0, 'column': 1})
        # generate empty pilot_list
        self.pilot_list = PilotList(self.bottom_frame, self.ship_id,
                                    grid_params={'row': 1, 'column': 1, 'sticky': 'n', 'rowspan': 2})

        self.update_ship_info(self.ship_id)

    def update_ship_info(self, ship_id):
        ship_basic_info = XwmDbQuery.get_ship_basic_info(ship_id)

        if not ship_basic_info:
            return False

        firing_arcs_string = ''
        firing_arcs_list = XwmDbQuery.get_ship_firing_arcs(ship_id)
        if not firing_arcs_list:
            firing_arcs_string = 'No Firing Arc'
        for arc in firing_arcs_list:
            firing_arcs_string += arc['firing_arc_name'] + ',\n'
        firing_arcs_string = firing_arcs_string.strip().strip(',')

        self.fields[0].config(text=ship_basic_info['ship_name'])
        self.fields[1].config(text=ship_basic_info['faction_name'])
        self.fields[2].config(text=ship_basic_info['ship_size'])
        self.fields[3].config(text=firing_arcs_string)

        self.ship_stats.update_ship_stats(ship_id)
        self.action_bar.update_action_bar(ship_id)
        self.upgrade_bar.update_upgrade_bar(ship_id)
        self.maneuver_dial.update_dial(ship_id)
        self.pilot_list.update_pilot_list(ship_id)

    def __generate_headers_and_fields(self):
        for i in range(4):
            self.headers.append(ttk.Label(self.basic_info_frame, style='Header.ShipInfo.TLabel'))

        self.headers[0].config(text='Name:')
        self.headers[0].grid(row=0, column=0, sticky='nsew')
        self.headers[1].config(text='Faction:')
        self.headers[1].grid(row=0, column=2, sticky='nsew')
        self.headers[2].config(text='Size:')
        self.headers[2].grid(row=1, column=0, sticky='nsew')
        self.headers[3].config(text='Firing Arcs:')
        self.headers[3].grid(row=1, column=2, sticky='nsew')

        for i in range(4):
            self.fields.append(ttk.Label(self.basic_info_frame, style='ShipInfo.TLabel'))
        self.fields[3].config(**self.options['firing_arcs.ship_info'])

        self.fields[0].grid(row=0, column=1, sticky='nsew')
        self.fields[1].grid(row=0, column=3, sticky='nsew')
        self.fields[2].grid(row=1, column=1, sticky='nsew')
        self.fields[3].grid(row=1, column=3, sticky='nsew')


if __name__ == '__main__':
    shipId = 5
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    ShipInfo(app, ship_id=shipId)
    root.mainloop()
