import tkinter as tk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery
from ship_stats import ShipStats
from action_bar import ActionBar
from upgrade_bar import UpgradeBar
from pilot_list import PilotList
from maneuver_dial import ManeuverDial


class ShipInfo(tk.Frame):
    def __init__(self, master, ship_name='', ship_id=0, pack_params=None, grid_params=None):
        tk.Frame.__init__(self, master)
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')

        self.ship_name = ship_name
        self.ship_id = ship_id

        self.basic_info_frame = tk.Frame(self)
        self.basic_info_frame.pack(side='top')
        self.name_label = tk.Label(self.basic_info_frame, relief='raised')
        self.name_label.grid(row=0, column=0, sticky='nsew')
        self.faction_menu = tk.Label(self.basic_info_frame, relief='raised')
        self.faction_menu.grid(row=0, column=1, sticky='nsew')
        self.ship_size_label = tk.Label(self.basic_info_frame, relief='raised')
        self.ship_size_label.grid(row=1, column=0, sticky='nsew')
        self.firing_arc_label = tk.Label(self.basic_info_frame, relief='raised')
        self.firing_arc_label.grid(row=1, column=1, sticky='nsew')

        # generate blank ship_stats
        self.ship_stats = ShipStats(self, self.ship_id)
        # generate blank action_bar
        self.action_bar = ActionBar(self, self.ship_id)
        # generate blank upgrade_bar
        self.upgrade_bar = UpgradeBar(self, self.ship_id)
        # generate empty pilot_list
        self.pilot_list = PilotList(self, self.ship_id)
        # generate empty maneuver_dial
        self.maneuver_dial = ManeuverDial(self, self.ship_id)

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
            firing_arcs_string += arc['firing_arc_name'] + ', '
        firing_arcs_string = firing_arcs_string.strip().strip(',')

        self.name_label.config(text=ship_basic_info['ship_name'])
        self.faction_menu.config(text=ship_basic_info['faction_name'])
        self.ship_size_label.config(text=ship_basic_info['ship_size'])
        self.firing_arc_label.config(text=firing_arcs_string)

        self.ship_stats.update_ship_stats(ship_id)
        self.action_bar.update_action_bar(ship_id)
        self.upgrade_bar.update_upgrade_bar(ship_id)
        self.pilot_list.update_pilot_list(ship_id)
        self.maneuver_dial.update_dial(ship_id)


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    ShipInfo(app, ship_id=shipId)
    root.mainloop()
