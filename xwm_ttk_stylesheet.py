from tkinter import ttk


class XwmTtkStylesheet:
    @staticmethod
    def get_style():
        s = ttk.Style()
        d = dict()

        s.configure('ManeuverDial.TLabel', foreground='grey', background='#262626', borderwidth='2', relief='sunken')
        d['label.maneuver_dial'] = {'anchor': 'center', 'compound': 'none'}
        s.configure('Blank.ManeuverDial.TLabel', foreground='grey')
        s.configure('Speed.ManeuverDial.TLabel', foreground='yellow')
        s.configure('Green.ManeuverDial.TLabel', foreground='green')
        s.configure('White.ManeuverDial.TLabel', foreground='white')
        s.configure('Red.ManeuverDial.TLabel', foreground='red')

        s.configure('PilotList.TLabel', font=('sans-serif', 8), padding=2, anchor='center')
        d['odd.pilot_list'] = {'background': 'wheat2'}
        d['even.pilot_list'] = {'background': 'wheat3'}
        s.configure('Regular.PilotList.TLabel', borderwidth=2, relief='raised', padx=3)
        s.configure('Header.Regular.PilotList.TLabel', background='wheat4', font=('sans-serif', 10))
        s.configure('PilotName.Header.Regular.PilotList.TLabel', anchor='w', padx=20, width=-20, wraplength='100p')
        d['p_name_frame.pilot_list'] = {'padding': 2}
        s.configure('PilotList.TFrame', relief='raised', borderwidth=2, width=-20)
        s.configure('Odd.PilotList.TFrame', background='wheat2')
        s.configure('Even.PilotList.TFrame', background='wheat3')
        s.configure('Unique.PilotList.TLabel', width=2)
        s.configure('PilotName.PilotList.TLabel', wraplength='105p', anchor='w')

        s.configure('UpgradeBar.TFrame', background='black', borderwidth=2)
        s.configure('Header.UpgradeBar.TLabel', background='dim gray', font=('sans-serif', 16))
        d['header.upgrade_bar'] = {'anchor': 'center'}
        s.configure('Slot.UpgradeBar.TLabel', background='snow3', font=('sans-serif', 7))
        d['slot.upgrade_bar'] = {'padding': 0, 'compound': 'none', 'anchor': 'center'}

        s.configure('ActionBar.TFrame', background='black')
        s.configure('Header.ActionBar.TLabel', background='dim gray', font=('sans-serif', 16))
        d['header.action_bar'] = {'anchor': 'center'}
        s.configure('Slot.ActionBar.TLabel', background='snow3', font=('sans-serif', 7))
        d['slot.action_bar'] = {'padding': 2, 'compound': 'none', 'anchor': 'center'}

        s.configure('ShipStats.TFrame', background='black')
        s.configure('ShipStats.TLabel', background='snow3', font=('sans-serif', 14), padx=10)
        s.configure('Header.ShipStats.TLabel', background='black', foreground='white', font=('sans-serif', 19))
        d['attack.ship_stats'] = {'foreground': 'red'}
        d['energy.ship_stats'] = {'foreground': '#202020'}
        d['agility.ship_stats'] = {'foreground': 'green'}
        d['hull.ship_stats'] = {'foreground': 'yellow'}
        d['shield.ship_stats'] = {'foreground': 'blue'}

        s.configure('ShipInfo.TLabel', background='light grey', foreground='black', font=('sans-serif', 10),
                    relief='raised', anchor='center', padding=4)
        s.configure('Header.ShipInfo.TLabel', background='slate grey', foreground='white', font=('sans-serif', 12))
        d['firing_arcs.ship_info'] = {}

        return d
