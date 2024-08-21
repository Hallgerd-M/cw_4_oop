import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy(
        "1",
        "Vacancy",
        {"from": 50000, "to": 60000, "currency": "RUR"},
        "URL",
        "Experience",
        "Employment",
        "Description",
    )


@pytest.fixture
def vacancy2():
    return Vacancy(
        "2",
        "Vacancy2",
        {"from": None, "to": 60000, "currency": "RUR"},
        "URL2",
        "Experience2",
        "Employment2",
        "Description2",
    )


@pytest.fixture
def vacancy3():
    return Vacancy(
        "3",
        "Vacancy",
        {"from": 50000, "to": None, "currency": "BYR"},
        "URL",
        "Experience",
        "Employment",
        "Description",
    )


@pytest.fixture
def vacancy4():
    return Vacancy(
        "4", "Vacancy", None, "URL", "Experience", "Employment", "Description"
    )


def test_vacancy_init(vacancy1, vacancy2, vacancy4):
    assert vacancy1.name == "Vacancy"
    assert vacancy1.get_id == "1"
    assert vacancy1.salary == {"from": 50000, "to": 60000, "currency": "RUR"}
    assert vacancy1.url == "URL"
    assert vacancy1.experience == "Experience"
    assert vacancy1.employment == "Employment"
    assert vacancy1.description == "Description"

    assert vacancy2.name == "Vacancy2"
    assert vacancy2.get_id == "2"
    assert vacancy2.salary == {"from": None, "to": 60000, "currency": "RUR"}

    assert vacancy4.salary is None


def test_str(vacancy1):
    vacancy1.salary_valid()
    assert (
        str(vacancy1)
        == "Вакансия номер 1 'Vacancy' c зарплатой 50000 - 60000 RUR.\nСсылка на вакансию: URL\nОпыт работы: Experience. Занятость: Employment.\nОписание: Description.\n"
    )


def test_salary_valid(vacancy1, vacancy2, vacancy3, vacancy4):
    vacancy1.salary_valid()
    vacancy2.salary_valid()
    vacancy3.salary_valid()
    vacancy4.salary_valid()
    assert vacancy1.salary == "50000 - 60000 RUR"
    assert vacancy2.salary == "до 60000 RUR"
    assert vacancy3.salary == "от 50000 BYR"
    assert vacancy4.salary == "(не указана)"


@pytest.fixture
def vacancy5():
    return Vacancy(
        "1", "Vacancy1", None, "url", "experience", "employment", "description"
    )


@pytest.fixture
def vacancy6():
    return Vacancy(
        "2",
        "Vacancy2",
        {"from": None, "to": 7, "currency": "BYR"},
        "url",
        "experience",
        "employment",
        "description",
    )


@pytest.fixture
def vacancy7():
    return Vacancy(
        "3",
        "Vacancy3",
        {"from": None, "to": 7, "currency": "RUR"},
        "url",
        "experience",
        "employment",
        "description",
    )


@pytest.fixture
def vacancy8():
    return Vacancy(
        "4",
        "Vacancy4",
        {"from": 3, "to": 7, "currency": "RUR"},
        "url",
        "experience",
        "employment",
        "description",
    )


def test_gt_dif_currencies(vacancy5, vacancy6):
    result = vacancy5 > vacancy6
    assert result == "Сравниваются зарплаты в разных валютах"


def test_gt_price_none(vacancy5, vacancy7):
    result1 = vacancy5 > vacancy7
    assert (
        result1
        == "Зарплата вакансии 1 'Vacancy1' меньше, чем зарплата вакансии 3 'Vacancy3'"
    )


def test_gt(vacancy7, vacancy8):
    result2 = vacancy7 > vacancy8
    assert (
        result2
        == "Зарплата вакансии 3 'Vacancy3' больше, чем зарплата вакансии 4 'Vacancy4'"
    )
