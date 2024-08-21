from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """Абстрактный родительский класс для работы с API"""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_response(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs) -> Any:
        pass
