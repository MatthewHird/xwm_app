from PIL import Image, ImageTk


class ActionIcons:
    def __init__(self):
        self.icon_image = {}
        self.icon_photo_image = {}
        icon_list_file = open('action_images/action_images_list.txt', 'r')
        icon_list = icon_list_file.read().split('\n')
        icon_list_file.close()

        for entry in icon_list:
            file_string = 'action_images/' + entry.replace('_', '-') + '.png'
            self.icon_image[entry] = Image.open(file_string)
            self.icon_photo_image[entry] = ImageTk.PhotoImage(self.icon_image[entry])

    def get_icon(self, icon_name):
        return self.icon_photo_image[icon_name]


class ManeuverIcons:
    def __init__(self):
        self.icon_image = {}
        self.icon_photo_image = {}
        icon_list_file = open('maneuver_images/maneuver_images_list.txt', 'r')
        icon_list = icon_list_file.read().split('\n')
        icon_list_file.close()

        for entry in icon_list:
            file_string = 'maneuver_images/' + entry.replace('_', '-') + '.png'
            self.icon_image[entry] = Image.open(file_string)
            self.icon_photo_image[entry] = ImageTk.PhotoImage(self.icon_image[entry])

    def get_icon(self, icon_name):
        return self.icon_photo_image[icon_name]


class UpgradeIcons:
    def __init__(self):
        self.icon_image = {}
        self.icon_photo_image = {}
        icon_list_file = open('upgrade_images/upgrade_images_list.txt', 'r')
        icon_list = icon_list_file.read().split('\n')
        icon_list_file.close()

        for entry in icon_list:
            file_string = 'upgrade_images/' + entry.replace('_', '-') + '.png'
            self.icon_image[entry] = Image.open(file_string)
            self.icon_photo_image[entry] = ImageTk.PhotoImage(self.icon_image[entry])

    def get_icon(self, icon_name):
        return self.icon_photo_image[icon_name]