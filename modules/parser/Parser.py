

class Parser:
    def __init__(self):
        self.__settings = None
        self.__version:str = ""
        self.__status:bool = False

    def __config_init(self, config):
        try:
            self.__settings = config["settings"]
            self.__status = True
        except KeyError as error:
            print(error)

    def start(self, **config):
        self.__config_init(config)

    def parse(self, url:str): ...

    @property
    def version(self) -> str: return self.__version

    @property
    def status(self) -> bool: return self.__status
