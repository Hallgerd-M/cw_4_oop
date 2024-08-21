import json
from typing import Any, List


class Vacancy:
    """Класс для работы с вакансиями:"""

    __slots__ = (
        "name",
        "__id",
        "salary",
        "url",
        "description",
        "experience",
        "employment",
    )

    def __init__(
        self,
        id: str,
        name: str,
        salary: Any,
        url: str,
        experience: str,
        employment: str,
        description: str,
    ) -> None:
        self.name = name
        self.__id = id
        self.salary = salary
        self.url = url
        self.description = description
        self.experience = experience
        self.employment = employment

    @property
    def get_id(self) -> str:
        """Геттер: возвращает id вакансии"""
        return self.__id

    def __str__(self) -> str:
        self.salary_valid()
        return f"Вакансия номер {self.get_id} '{self.name}' c зарплатой {self.salary}.\nСсылка на вакансию: {self.url}\nОпыт работы: {self.experience}. Занятость: {self.employment}.\nОписание: {self.description}.\n"

    def salary_valid(self) -> Any:
        """Метод для валидации данных по зарплате"""
        if self.salary is None:
            self.salary = "(не указана)"
        elif self.salary["to"] is None:
            self.salary = f"от {self.salary["from"]} {self.salary["currency"]}"
        elif self.salary["from"] is None:
            self.salary = f"до {self.salary["to"]} {self.salary["currency"]}"
        elif self.salary["to"] is not None and self.salary["from"] is not None:
            self.salary = (
                f"{self.salary["from"]} - {self.salary["to"]} {self.salary["currency"]}"
            )

    def __gt__(self, other) -> str:
        """Метод для сравнения зарплат двух вакансий (в случае указаниия вилки зп,
        высчитывает среднее арифметическое)"""
        if self.salary is None:
            self.salary = 0
        elif self.salary["currency"] != "RUR":
            self.salary = 0
            return "Сравниваются зарплаты в разных валютах"
        elif self.salary["to"] is None:
            self.salary = self.salary["from"]
        elif self.salary["from"] is None:
            self.salary = self.salary["to"]
        elif self.salary["to"] is not None and self.salary["from"] is not None:
            self.salary = (self.salary["from"] + self.salary["to"]) / 2

        if other.salary is None:
            other.salary = 0
        elif other.salary["currency"] != "RUR":
            other.salary = 0
            return "Сравниваются зарплаты в разных валютах"
        elif other.salary["to"] is None:
            other.salary = other.salary["from"]
        elif other.salary["from"] is None:
            other.salary = other.salary["to"]
        elif other.salary["to"] is not None and other.salary["from"] is not None:
            other.salary = other.salary["from"] + other.salary["to"] / 2

        if self.salary > other.salary:
            return f"Зарплата вакансии {self.get_id} '{self.name}' больше, чем зарплата вакансии {other.get_id} '{other.name}'"
        else:
            return f"Зарплата вакансии {self.get_id} '{self.name}' меньше, чем зарплата вакансии {other.get_id} '{other.name}'"

    def get_top_vacancies(self, top_number: int, vac_dict_list: List) -> List:
        """Метод для выведения N топ вакансий по зарплате"""
        for vac_dict in vac_dict_list:
            if vac_dict["salary"] is None:
                vac_dict["avg_salary"] = 0
            elif vac_dict["salary"]["to"] is None:
                vac_dict["avg_salary"] = vac_dict["salary"]["from"]
            elif vac_dict["salary"]["from"] is None:
                vac_dict["avg_salary"] = vac_dict["salary"]["to"]
            elif (
                vac_dict["salary"]["to"] is not None
                and vac_dict["salary"]["from"] is not None
            ):
                vac_dict["avg_salary"] = (
                    vac_dict["salary"]["from"] + vac_dict["salary"]["to"]
                ) / 2
        sorted_vacancies = sorted(
            vac_dict_list, key=lambda vacancy: vacancy["avg_salary"]
        )
        return sorted_vacancies[:top_number]


if __name__ == "__main__":
    with open("../data/vac1.json", encoding="utf-8") as f:
        file1 = json.load(f)
    # print(file1[2]["salary"])
    vac_1 = Vacancy(
        file1[2]["id"],
        file1[2]["name"],
        {"from": 4, "to": 6, "currency": "RUR"},
        file1[2]["url"],
        file1[2]["experience"],
        file1[2]["employment"],
        file1[2]["description"],
    )
    vac_2 = Vacancy(
        file1[4]["id"],
        file1[4]["name"],
        {"from": None, "to": 6, "currency": "BYR"},
        file1[4]["url"],
        file1[4]["experience"],
        file1[4]["employment"],
        file1[4]["description"],
    )
    result = vac_1 > vac_2
    print(result)
    # print(vac_1.salary)
    # print(vac_2.salary)
