import pytest


# Представим ситуацию – мы работаем с очень простыми функциями, которые работают со списками словарей.
# Например, такого формата: [{ "name": ... , "family_name": ..., "title": ...,  "skills": [...] }, ... ]


def get_names_from_persons(persons):
    """ Возвращает имена"""
    return [person["name"] for person in persons]


def get_skills_from_persons(persons):
    """ Возвращает все новыки"""
    skills = set()
    for person in persons:
        skills.update(person["skills"])
    return list(skills)


def count_persons(persons):
    """ Возвращает должности"""
    return len(persons)


class TestPersonsFunctions:

    @pytest.fixture
    def persons(self):
        return [
            {
                "name": "Alfonsa", "family_name": "Ruiz", "title": "Senior Software Engineer",
                "skills": ["python", "go", "sql"],
            },
            {
                "name": "Sayid", "family_name": "Khan", "title": "Project Manager",
                "skills": ["java", "spring", "html", "sql"],
            },
        ]

    def test_get_names_from_persons(self, persons):
        assert get_names_from_persons(persons) == ["Alfonsa", "Sayid"]

    def test_get_skills_from_persons(self, persons):

        result = get_skills_from_persons(persons)
        assert type(result) == list
        assert set(result) == {"python", "go", "sql", "java", "spring", "html"}

    def test_count_persons(self, persons):
        assert count_persons(persons) == 2

# https://realpython.com/pytest-python-testing/#when-to-create-fixtures
