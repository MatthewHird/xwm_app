import tkinter as tk
from tkinter import ttk
from global_environment import GlobalEnvironment


class AppWindow(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        GlobalEnvironment.set_master_frame(master)
        self.pack()
        self.pack_propagate(1)


if __name__ == '__main__':
    root = tk.Tk()
    app = AppWindow(root)
    root.mainloop()
