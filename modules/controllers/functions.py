from os import remove, makedirs
from os.path import abspath, exists, getsize
from json import dump, load
from typing import Literal
from ..errors.Errors import NotFoundError


def trim(text:str) -> str:
    return " ".join(text.split())


def lower(text:str) -> str:
    return text.lower()


def command(text:str) -> str:
    return lower(trim(text))


def load_datas(path:str):
    try:
        with open(path, "r") as file:
            return load(file)
    except FileNotFoundError:
        raise NotFoundError(value=path, function_name="load datas")


def _convert_unit(size:int | float, unit_format:Literal["B"] = "MB") -> dict:
    units_information = {"B": 1/8, "BT":1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3, "TB": 1024 ** 4}
    return {"size": round(size / units_information[unit_format]), "unit": unit_format} if unit_format in units_information \
        else {"size":size, "unit":f"Not Supported Format: [{unit_format}]"}


def size_percentage_calc(new_size:int, old_size:int) -> int:
    percentage = round(((new_size / old_size) * 100))
    return percentage - 100 if old_size > new_size else 100 - percentage


def get_file_size(file_path: str, file_name: str, file_format: str, unit_format:Literal["B"] = "MB") -> dict:
    size = getsize(f"{file_path}\\{file_name}.{file_format}")
    return _convert_unit(size=size,unit_format=unit_format)


def find_path(path:str):
    return exists(path)


def alias(path:str):
    return abspath(path)


def write_datas(path:str, datas:dict):
    try:
        with open(path, "w") as file:
            dump(datas, file, indent=2, ensure_ascii=False)
    except FileNotFoundError:
        raise NotFoundError(value=path, function_name="write datas")


def create_json(folder_directory:str,file_name:str):
    path = f"{folder_directory}/{file_name}.json"
    write_datas(path=path, datas={})


def delete_json(folder_directory:str,file_name:str):
    remove(f"{folder_directory}\\{file_name}")


def create_folder(folder_directory:str,folder_name:str):
    try:
        makedirs(f"{folder_directory}\\{folder_name}")
    except FileNotFoundError:
        raise NotFoundError(value=folder_name, function_name="create folder")
