from ..fileworker.FileWorker import JsonFileWorker
from ..moviepy.MoviePython import MoviePython
from ..parser.Parser import Parser
from ..tkinter.Tkinter import Tkinter
from ..pystray.Pystray import Pystray


class Services(JsonFileWorker, MoviePython, Parser):
    r"""
    Сервисы - модуль, наследующий свойства и методы всех модулей,
    участвующих в работе программы.
    Программа не будет работать, если сервис fileworker не инициализируется!
    """
    def __init__(self):
        r"""Общая инициализация модулей для дальнейшей работы с ними"""
        super().__init__()
        self.fileworker = JsonFileWorker()
        self.moviepy = MoviePython()
        self.parser = Parser()
        #self.pystray = Pystray()
        #self.tkinter = Tkinter()
        self.__services_status = {
            "fileworker": False,
            "database": False,
            "tkinter": False,
            "parser": False,
            "pystray": False,
            "ai": False,
            "pillow": False,
            "moviepy": False,
        }

    def __service_status_update(self):
        self.__services_status["fileworker"] = self.fileworker.status
        self.__services_status["moviepy"] = self.moviepy.status
        self.__services_status["parser"] = self.parser.status
        #self.__services_status["pystray"] = self.pystray.status
        #self.__services_status["tkinter"] = self.tkinter.status

    def __service_init(self):
        r"""Осуществляет инициализацию всех модулей"""
        # Starting a file service
        self.fileworker.start()

        # Loading configuration
        moviepy_config = self.fileworker.get_config_key("moviepy.config")
        parser_config = self.fileworker.get_config_key("parser.config")
        #tkinter_config = self.fileworker.get_config_key("tkinter.config")
        #pystray_config = self.fileworker.get_config_key("pystray.config")

        # = self.__main_window

        # Initializing services
        self.moviepy.start(**moviepy_config)
        self.parser.start(**parser_config)
        #self.tkinter.start(**tkinter_config)
        #self.pystray.start(**pystray_config)

        # Update service status
        self.__service_status_update()

    def start(self):
        r"""Запускает инициализацию сервиса"""
        self.__service_init()
        #self.tkinter.mainloop()

    @property
    def status(self):
        r"""Возвращает статус всех сервисов"""
        return self.__services_status

    def information(self):
        r"""Предоставляет табличную информацию о статусах сервиса"""
        for service, status in self.__services_status.items():
            print(f"Service: {service} | Status: {status}")


