from sys import exit
from pystray import Icon, Menu, MenuItem
from PIL import Image
from ..controllers.functions import alias


class Pystray:
    def __init__(self):
        self.__paths: dict | None = None
        self.__icons: dict | None = None
        self.__menu: dict | None = None
        self.__app_image: str | None = None
        self.__app_icon: str | None = None
        self.__status = False

    def __config_init(self, config):
        self.__paths = config.get("paths")
        self.__icons = config.get("icons")
        self.__menu = config.get("menu")
        self.__paths["general"] = alias(self.__paths.get("general"))
        self.__app_image = Image.open(f"{self.__paths.get("general")}\\{self.__paths.get("icons")}\\{self.__icons.get("app_logo")}")
        self.__app_icon = Icon("Fire Star", self.__app_image, menu=Menu(
            MenuItem("Exit", self.on_click),
            MenuItem("Settings (wip)", self.on_click),
            MenuItem("Services", Menu(
                MenuItem("MoviePy", self.on_click),
                MenuItem("Pillow", self.on_click),
                MenuItem("Parser", self.on_click),
                MenuItem("Waifu2x", self.on_click),
                MenuItem("Parser", self.on_click),
                MenuItem("Data Base", self.on_click),
            )),
            MenuItem("Assets", Menu(
                MenuItem("Images", self.on_click),
                MenuItem("Videos", self.on_click),
            )),
            MenuItem("Theme", Menu(
                MenuItem("Light", self.on_click),
                MenuItem("Dark", self.on_click),
                MenuItem("System", self.on_click),
            )),
        ))
        self.__app_icon.run()
        self.__status = True

    def start(self, **config):
        self.__config_init(config)

    def on_click(self, icon, item):
        if str(item) == "Exit":
            icon.stop()

    @property
    def status(self): return self.__status

