from typing import List


def get_top_vacancies(top_number: int, vac_dict_list: List) -> List:
    """Метод для выведения N топ вакансий по зарплате"""
    for vac_dict in vac_dict_list:
        if vac_dict["salary"] is None:
            vac_dict["avg_salary"] = 0
        elif vac_dict["salary"]["currency"] != "RUR":
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
        vac_dict_list, key=lambda vacancy: vacancy["avg_salary"], reverse=True
    )
    return sorted_vacancies[:top_number]


dict_list = [
    {"id": 1, "salary": {"from": 50000, "to": 60000}},
    {"id": 2, "salary": {"from": 50000, "to": None}},
    {"id": 3, "salary": {"from": None, "to": 60000}},
    {"id": 4, "salary": {"from": 100000, "to": 110000}},
    {"id": 5, "salary": None},
]

if __name__ == "__main__":
    result = get_top_vacancies(5, dict_list)
    print(result)
