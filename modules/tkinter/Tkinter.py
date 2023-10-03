import customtkinter
from .components.atoms.Buttons.Button import Button
# from screeninfo import get_monitors
# x_pos = round(((self.__screen.width / 2) - geometry["width"] / 2))
# y_pos = round(((self.__screen.height / 2) - geometry["height"] / 2))


class Tkinter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.Button = None
        self.__screen: dict | None = None
        self._status = False

        self.__settings:dict | None = None

    def __config_init(self, config):
        self.__settings = config["settings"]
        #self.__screen = list(filter(lambda screen: screen.is_primary,get_monitors()))[0]

    def __window_init(self, title:str, geometry:dict, resizable:dict):
        self.title(title)
        self.geometry(f"{geometry["width"]}x{geometry["height"]}")
        self.resizable(width=resizable["width"], height=resizable["height"])
        self.Button.__init__(width=142, height=142, text="hello", x_pos=0.5, y_pos=0.5)
        customtkinter.set_appearance_mode(self.__settings["theme"])

    def start(self, **config):
        self.__config_init(config)
        self.__window_init(title=self.__settings["title"], geometry=self.__settings["geometry"], resizable=self.__settings["resizable"])
        self.mainloop()
