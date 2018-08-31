import tkinter as tk
from window import Window
from maneuver_dial import ManeuverDial


class ManeuverViewer(tk.Frame):

    def __init__(self, master, pack_side='top', grid_pos=None):
        tk.Frame.__init__(self, master)
        if grid_pos:
            self.grid(row=grid_pos[0], column=grid_pos[1])
        else:
            self.pack(side=pack_side)

        self.maneuver_table = ManeuverDial(self, 'Protectorate Starfighter', pack_side='bottom')

        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side='top')

        self.input_frame_header = tk.Label(self.input_frame, text='Ship Name: ')
        self.input_frame_header.grid(row=0, column=0)

        self.input_frame_entry = tk.Entry(self.input_frame)
        self.input_frame_entry.grid(row=0, column=1)

        self.input_frame_button = tk.Button(self.input_frame, text='Display Maneuver Table',
                                            command=self.display_maneuver_table)
        self.input_frame_button.grid(row=0, column=2)

    def display_maneuver_table(self):
        if not self.maneuver_table.update_dial(self.input_frame_entry.get()):
            temp_text = self.input_frame_button.cget('text')
            temp_bg = self.input_frame_button.cget('bg')
            temp_active_bg = self.input_frame_button.cget('activebackground')
            self.input_frame_button.config(text='Invalid Ship Type', bg='red', activebackground='maroon')
            self.input_frame_button.flash()
            self.input_frame_button.flash()
            self.input_frame_button.flash()
            self.input_frame_button.config(text=temp_text, bg=temp_bg, activebackground=temp_active_bg)


if __name__ == '__main__':
    root = tk.Tk()
    app = Window(root)
    ManeuverViewer(app)
    root.mainloop()
