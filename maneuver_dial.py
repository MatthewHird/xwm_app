import tkinter as tk
from app_window import AppWindow
from xwm_icons import ManeuverIcons
from xwm_db_query import XwmDbQuery


class ManeuverDial(tk.Frame):
    def __init__(self, master, ship_id=0, pack_side='top', grid_pos=None):
        tk.Frame.__init__(self, master, bg='black')
        self.maneuver_icons = ManeuverIcons()
        if grid_pos:
            self.grid(row=grid_pos[0], column=grid_pos[1])
        else:
            self.pack(side=pack_side)

        self.config_table = None
        self.maneuver_table = []

        for i in range(6):
            self.maneuver_table.append([])
            for j in range(9):
                self.maneuver_table[i].append(tk.Label(self, image=self.maneuver_icons.get_icon('blank_icon'), text='.',
                                                       fg='grey', bg='#262626', bd='2', relief='sunken'))

        self.__generate_speed_labels()
        self.update_dial(ship_id)

    def update_dial(self, ship_id):
        dial_list = XwmDbQuery.get_maneuver_dial(ship_id)

        if not dial_list:
            return False

        self.__generate_config_table()
        for maneuver in dial_list:
            self.__generate_maneuver_label_config(maneuver['speed'], maneuver['maneuver_id'], maneuver['difficulty_char'])

        self.__update_maneuver_table()

        for i in range(6):
            for j in range(9):
                self.maneuver_table[i][j].grid(row=i, column=j)

        self.__check_empty_rows_and_cols()
        return True

    def __generate_speed_labels(self):
        self.maneuver_table[0][0].config(image=self.maneuver_icons.get_icon('speed_five'), text='FIVE', fg='white')
        self.maneuver_table[1][0].config(image=self.maneuver_icons.get_icon('speed_four'), text='FOUR', fg='white')
        self.maneuver_table[2][0].config(image=self.maneuver_icons.get_icon('speed_three'), text='THREE', fg='white')
        self.maneuver_table[3][0].config(image=self.maneuver_icons.get_icon('speed_two'), text='TWO', fg='white')
        self.maneuver_table[4][0].config(image=self.maneuver_icons.get_icon('speed_one'), text='ONE', fg='white')
        self.maneuver_table[5][0].config(image=self.maneuver_icons.get_icon('speed_zero'), text='ZERO', fg='white')

    def __generate_config_table(self):
        self.config_table = []

        for i in range(6):
            self.config_table.append([])
            for j in range(9):
                self.config_table[i].append({'image': self.maneuver_icons.get_icon('blank_icon'),
                                             'text': '.', 'fg': 'grey'})

    def __generate_maneuver_label_config(self, speed, maneuver_type_id, difficulty):
        row = 5 - speed
        col = None
        maneuver_type = None
        color = None
        text = str(speed)

        if maneuver_type_id == 1:
            col = 1
            maneuver_type = 'turn_left'
            text += '-TL'
        elif maneuver_type_id == 2:
            col = 2
            maneuver_type = 'bank_left'
            text += '-BL'
        elif maneuver_type_id == 3:
            col = 3
            maneuver_type = 'straight_move'
            text += '-SM'
        elif maneuver_type_id == 4:
            col = 4
            maneuver_type = 'bank_right'
            text += '-BR'
        elif maneuver_type_id == 5:
            col = 5
            maneuver_type = 'turn_right'
            text += '-TR'
        elif maneuver_type_id == 6:
            col = 7
            maneuver_type = 'k_turn'
            text += '-KT'
        elif maneuver_type_id == 7:
            col = 6
            maneuver_type = 's_loop_left'
            text += '-SLL'
        elif maneuver_type_id == 8:
            col = 8
            maneuver_type = 's_loop_right'
            text += '-SLR'
        elif maneuver_type_id == 9:
            col = 6
            maneuver_type = 't_roll_left'
            text += '-TRL'
        elif maneuver_type_id == 10:
            col = 8
            maneuver_type = 't_roll_right'
            text += '-TRR'
        elif maneuver_type_id == 11:
            col = 3
            maneuver_type = 'stationary'
            text += '-ST'
        elif maneuver_type_id == 12:
            col = 7
            maneuver_type = 'reverse_straight_move'
            text += '-RSM'
        elif maneuver_type_id == 13:
            col = 6
            maneuver_type = 'reverse_bank_left'
            text += '-RBL'
        elif maneuver_type_id == 14:
            col = 8
            maneuver_type = 'reverse_bank_right'
            text += '-RBR'

        if difficulty == 'G':
            color = 'green'
            maneuver_type += '_green'
            text += '-G'
        elif difficulty == 'W':
            color = 'white'
            maneuver_type += '_white'
            text += '-W'
        elif difficulty == 'R':
            color = 'red'
            maneuver_type += '_red'
            text += '-R'

        self.config_table[row][col] = {'image': self.maneuver_icons.get_icon(maneuver_type), 'text': text, 'fg': color}

    def __update_maneuver_table(self):
        for i in range(6):
            for j in range(1, 9):
                if self.maneuver_table[i][j].cget('text') != self.config_table[i][j]['text']:
                    self.maneuver_table[i][j].grid_forget()
                    self.maneuver_table[i][j].config(self.config_table[i][j])

    def __check_empty_rows_and_cols(self):

        for i in range(6):
            empty = True
            for j in range(1, 9):
                if self.maneuver_table[i][j].cget('text') != '.':
                    empty = False
            if empty:
                for k in range(9):
                    self.maneuver_table[i][k].grid_forget()
        for j in range(1, 9):
            empty = True
            for i in range(6):
                if self.maneuver_table[i][j].cget('text') != '.':
                    empty = False
            if empty:
                for k in range(6):
                    self.maneuver_table[k][j].grid_forget()


if __name__ == '__main__':
    shipId = 1
    root = tk.Tk()
    root.title(XwmDbQuery.get_ship_name(shipId))
    app = AppWindow(root)
    ManeuverDial(app, shipId)
    root.mainloop()
