import customtkinter
from customtkinter import CTkButton

SOCIALS = {
    "GitHub":"https://github.com/LiterTeams",
    "Discord":"https://discord.new/EJxzPSCPffUg",
    "YouTube":"https://www.youtube.com/@LiterTeams",
    "Vk":"https://vk.com/id141459067",
}


class Tkinter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.__screen: dict | None = None
        self.__version:str = ""
        self.__status:bool = False

        self.__settings:dict | None = None

    def __config_init(self, config):
        self.__settings = config["settings"]
        self.__status = True

    def __window_init(self, title:str, geometry:dict, resizable:dict):
        self.title(title)
        self.geometry(f"{geometry["width"]}x{geometry["height"]}")
        self.resizable(width=resizable["width"], height=resizable["height"])
        customtkinter.set_appearance_mode(self.__settings["theme"])

    def __header_init(self):
        self.navigation = customtkinter.CTkFrame(self, width=256, height=1044, bg_color="#131111")
        self.navigation.grid(row=0, column=0, padx=0, pady=(24,0), sticky="nsw")
        self.button_moviepy = CTkButton(self.navigation, text="MoviePy")
        self.button_pillow = CTkButton(self.navigation, text="Pillow")
        self.button_parser = CTkButton(self.navigation, text="Parser")
        self.button_waifu2x = CTkButton(self.navigation, text="Waifu2x")
        self.button_litecore = CTkButton(self.navigation, text="LiteCore")
        self.button_database = CTkButton(self.navigation, text="DataBase")
        self.button_settings = CTkButton(self.navigation, text="Settings")

    @staticmethod
    def option_menu_callback(self, choice):
        print(f"dropdown click: {choice}")

    def start(self, **config):
        self.__config_init(config)
        self.__window_init(title=self.__settings["title"], geometry=self.__settings["geometry"], resizable=self.__settings["resizable"])
        self.__header_init()
        self.mainloop()

    @property
    def version(self) -> str: return self.__version

    @property
    def status(self) -> bool: return self.__status
