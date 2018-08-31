import tkinter as tk
from window import Window
from maneuver_viewer import ManeuverViewer


class Main:
    @staticmethod
    def run():
        root = tk.Tk()
        app = Window(root)
        ManeuverViewer(app)
        root.mainloop()


if __name__ == '__main__':
    Main.run()
