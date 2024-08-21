import pytest

from src.get_top_vacancies import get_top_vacancies


@pytest.fixture
def vac_dict_list():
    return [
        {"id": 1, "salary": {"from": 50000, "to": 60000}},
        {"id": 2, "salary": {"from": 50000, "to": None}},
        {"id": 3, "salary": {"from": None, "to": 60000}},
        {"id": 4, "salary": {"from": 100000, "to": 110000}},
        {"id": 5, "salary": None},
    ]


@pytest.fixture
def top_number():
    return 4


def test_get_top_vacancies(top_number, vac_dict_list):
    print(get_top_vacancies(top_number, vac_dict_list))
    # assert get_top_vacancies(top_number, vac_dict_list) == [{"id": 4, "salary": {"from": 100000, "to": 110000}},
    #                                                  {"id": 3,  "salary": {"from": None, "to": 60000}},
    #                                                 {"id": 1,  "salary": {"from": 50000, "to": 60000}},
    #                                                {"id": 2,  "salary": {"from": 50000, "to": None}}]
