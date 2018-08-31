import tkinter as tk


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.pack_propagate(1)


if __name__ == '__main__':
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
