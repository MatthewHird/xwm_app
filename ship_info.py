import tkinter as tk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery
from ship_stats import ShipStats
from action_bar import ActionBar
from upgrade_bar import UpgradeBar
from pilot_list import PilotList
from maneuver_dial import ManeuverDial


class ShipInfo(tk.Frame):
    def __init__(self, master, ship_name='', ship_id=0, pack_side='top', grid_pos=None):
        tk.Frame.__init__(self, master)
        if grid_pos:
            self.grid(row=grid_pos[0], column=grid_pos[1])
        else:
            self.pack(side=pack_side)

        self.ship_name = ship_name
        self.ship_id = ship_id

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
