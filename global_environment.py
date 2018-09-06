from xwm_ttk_stylesheet import XwmTtkStylesheet


class GlobalEnvironment:
    master_frame = None
    current_screen = None
    stylesheet = None

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

    @classmethod
    def get_stylesheet(cls):
        if not cls.stylesheet:
            cls.stylesheet = XwmTtkStylesheet.get_style()
        return cls.stylesheet
