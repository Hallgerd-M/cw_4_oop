from abc import ABC, abstractmethod
from typing import Any


class WorkWithFiles(ABC):
    """Асбтрактный родительский класс для работы с файлами: записи полученных данных с сайта hh.ru в файл,
    получения ваканчий из файла по ключевым словам и удаления ваканчий по id"""

    @abstractmethod
    def save_to_json(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_data_from_json(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def delete_from_json(self, *args, **kwargs) -> Any:
        pass
