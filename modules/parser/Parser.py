

class Parser:
    def __init__(self):
        self.__settings = None
        self._status = False

    def __config_init(self, config):
        try:
            self.__settings = config["settings"]
            self._status = True
        except KeyError as error:
            print(error)

    def start(self, **config):
        self.__config_init(config)

    def parse(self, url:str): ...
