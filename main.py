import tkinter as tk
from app_window import AppWindow
from main_menu import MainMenu
from global_environment import GlobalEnvironment


class Main:
    def __init__(self):
        self.app = None
        self.root = None
        self.butt = None

    def run(self):
        self.root = tk.Tk()
        self.app = AppWindow(self.root)
        GlobalEnvironment.change_screen(MainMenu(GlobalEnvironment.get_master_frame()))
        self.root.mainloop()


if __name__ == '__main__':
    main = Main()
    main.run()
