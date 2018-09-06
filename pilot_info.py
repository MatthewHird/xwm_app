import tkinter as tk
from app_window import AppWindow
from xwm_db_query import XwmDbQuery
from ship_stats import ShipStats
from action_bar import ActionBar
from upgrade_bar import UpgradeBar
from pilot_list import PilotList
from maneuver_dial import ManeuverDial


class PilotInfo(tk.Frame):
    def __init__(self, master, pilot_name='', pilot_id=0, pack_params=None, grid_params=None):
        tk.Frame.__init__(self, master)
        if grid_params:
            self.grid(grid_params)
        elif pack_params:
            self.pack(pack_params)
        else:
            self.pack(side='top')


if __name__ == '__main__':
    pilotId = 5
    root = tk.Tk()
    root.title(XwmDbQuery.get_pilot_name(pilotId))
    app = AppWindow(root)
    PilotInfo(app, pilot_id=pilotId)
    root.mainloop()
