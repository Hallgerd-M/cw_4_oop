from typing import Any

import requests

from src.parser import Parser


class HH(Parser):
    """Класс для работы с API HeadHunter. Наследуется от абстрактного класса Parser"""

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def get_response(self) -> Any:
        """Функция подключения к API hh.ru"""
        response = requests.get(self.__url, headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_vacancies(
        self, keyword: str, per_page: int = 100, pages_number: int = 20
    ) -> Any:
        """Функция  получения данных с API hh.ru"""
        condition = self.get_response()
        if condition is True:
            self.params["text"] = keyword
            self.params["per_page"] = per_page
            while self.params.get("page") != pages_number:
                response = requests.get(
                    self.__url, headers=self.headers, params=self.params
                )
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1
        else:
            print("Ошибка получения данных")


if __name__ == "__main__":
    python1 = HH()
    result = python1.get_response()
    python1.get_vacancies("python", 1, pages_number=2)
    print(python1.vacancies)
