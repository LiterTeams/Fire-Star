from ..fileworker.FileWorker import JsonFileWorker
from ..moviepy.MoviePython import MoviePython
from ..parser.Parser import Parser
# from ..tkinter.Tkinter import Tkinter


class Services(JsonFileWorker, MoviePython, Parser):
    def __init__(self):
        super().__init__()
        self.fileworker = JsonFileWorker()
        self.moviepy = MoviePython()
        self.parser = Parser()
        #self.__tkinter = Tkinter()
        self._services_status = {
            "fileworker": self.fileworker._status,
            "database": False,
            "tkinter": False,
            "parser": self.parser._status,
            "ai": False,
            "pillow": False,
            "moviepy": self.moviepy._status,
        }

    def __service_init(self):
        # Starting a file service
        self.fileworker.start()

        # Loading configuration
        moviepy_config = self.fileworker.get_config_key("moviepy.config")
        parser_config = self.fileworker.get_config_key("parser.config")
        tkinter_config = self.__main_window = self.fileworker.get_config_key("tkinter.config")

        # Initializing services
        self.moviepy.start(**moviepy_config)
        self.parser.start(**parser_config)
        #self.__tkinter.start(**tkinter_config)

    def start(self):
        self.__service_init()

    def status(self):
        return self._services_status
