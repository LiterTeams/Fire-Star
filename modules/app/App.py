from ..services.Services import Services


class App(Services):
    r"""App - модуль, наследующий сервис со всеми его модулями."""
    def __init__(self):
        r"""Осуществляет инициализацию приложения"""
        super().__init__()
        self.services = Services()

    def start(self):
        r"""Осуществляет запуск приложения"""
        try:
            self.services.start()
            self.services.information()
        except KeyboardInterrupt:
            print("close")
