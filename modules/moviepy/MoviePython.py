from os import listdir
import moviepy.editor as moviepy
from colorama import init, Fore
from ..errors.Errors import NotFoundError, DuplicateError
from ..controllers.functions import get_file_size, size_percentage_calc, alias
from functools import reduce

init()


class MoviePython:

    def __init__(self):
        __slots__ = ("__settings","__supports","__paths","version")
        self.__settings:dict | None = None
        self.__supports:dict | None = None
        self.__paths:dict | None = None
        self.__files:list = []
        self.__version:str = ""
        self.__status = False

    def __config_init(self, config):
        try:
            print(reduce(lambda acc,res: dict(acc, **res),[{key:alias(value)} for key,value in config["paths"].items()]))
            self.__settings = config["settings"]
            self.__supports = config["supports"]
            self.__paths = reduce(lambda acc,res: dict(acc, **res),[{key:alias(value)} for key,value in config["paths"].items()])
            self.__version = config["version"]
            self.__status = True
        except KeyError as error:
            print(error)

    def start(self, **config): self.__config_init(config)

    def compression(self, file_path:str | None = None) -> None:
        if self.__files:
            try:
                for file_name in self.__files:
                    print(Fore.GREEN+f"Start compression video file: {Fore.GREEN+file_name}...")

                    file = moviepy.VideoFileClip(f"{file_path if file_path else self.__paths["video_path_get"]}\\{file_name}.mp4")
                    default_file_size = get_file_size(file_path=self.__paths["video_path_get"], file_name=file_name, file_format="mp4")

                    file.write_videofile(
                        filename=f"{self.__paths["video_path_put"]}\\{file_name}.mp4",
                        fps=self.__settings["fps"],
                        preset=self.__settings["preset"],
                        codec=self.__settings["codec"],
                    )

                    new_file_size = get_file_size(file_path=self.__paths["video_path_put"], file_name=file_name, file_format="mp4")

                    compression_percentage = size_percentage_calc(new_file_size["size"],default_file_size["size"])

                    print(Fore.GREEN+f"Default Size: {default_file_size['size']}{default_file_size['unit']} | New Size: {new_file_size['size']}{new_file_size['unit']} | Compression Percentage: {compression_percentage}% \n")
            except OSError:
                print(Fore.RED+f"Video File Not Found!")
        else:
            print(Fore.RED+"Files Not Found!")
        self.__files.clear()

    def auto_search(self):
        print(self.__paths)
        #files = list(filter(lambda elem: elem.endswith(".mp4"),listdir(f"{self.__paths.get("video_path_get")}")))
        #print(files)
        # if files:
        #     for file in files:
        #         file_name = file.split(".")[0]
        #         print(file_name)


    # getters | setters

    def set_settings(self, setting_name:str, setting_value:str) -> None:
        if setting_name not in self.__settings:
            raise NotFoundError(value=setting_name, function_name="MoviePython - set_settings")
        self.__settings[setting_name] = setting_value

    @property
    def status(self) -> bool: return self.__status

    @property
    def version(self) -> str: return self.__version

    @property
    def supports(self) -> dict: return self.__supports

    @property
    def paths(self) -> dict: return self.__paths

    @property
    def files(self) -> list: return self.__files

    @files.setter
    def files(self, file) -> None:
        if file in self.__files:
            raise DuplicateError(value=file, function_name="MoviePython - files.setter")
        print(Fore.BLUE + f"Uploading file: {file}...")
        self.__files.append(file)
        print(Fore.BLUE + f"File Upload Complete\n")

    @files.deleter
    def files(self) -> None: self.__files.clear()
