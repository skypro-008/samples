import json

import pytest

def get_next_pk(path):

    with open(path, encoding='utf-8') as file:
        full_data = json.load(file)

    last_element = full_data[-1]
    last_element_pk = last_element["pk"]
    next_pk = last_element_pk + 1

    return next_pk


@pytest.fixture
def new_data():

    path = "data.json"

    return  {
        "pk": get_next_pk(path),
        "full_name": "Bla bla bla ",
        "skills": ["Nothings"]
    }
