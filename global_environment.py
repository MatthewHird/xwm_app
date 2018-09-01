class GlobalEnvironment:
    master_frame = None
    current_screen = None

    @classmethod
    def set_master_frame(cls, master_frame):
        cls.master_frame = master_frame

    @classmethod
    def get_master_frame(cls):
        return cls.master_frame

    @classmethod
    def change_screen(cls, new_screen):
        if cls.current_screen:
            cls.current_screen.destroy()
        cls.current_screen = new_screen
