from ..services.Services import Services


class App(Services):
    def __init__(self):
        super().__init__()
        self.services = Services()

    def start(self):
        self.services.start()
