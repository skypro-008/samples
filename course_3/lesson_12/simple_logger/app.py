import logging
from flask import Flask, jsonify, request
from data import students
from loggers import create_and_set_loggers

create_and_set_loggers()

app = Flask(__name__)


logger = logging.getLogger("basic")
logger.debug("Неважное сообщение")
logger.warning("Запустились и работаем")

def get_one_by_pk(sequence, pk):
    """ Получаем одного студента"""
    logger.warning("Получаем одного студента")
    for s in sequence:
        if s["pk"] == pk:
            return s


def get_next_pk(sequence):
    new_pk = max(sequence, key=lambda x: x["pk"])["pk"] + 1
    return new_pk


@app.get('/students/')
def api_get_all():
    return jsonify(students), 200


@app.get('/students/<int:pk>')
def api_get_one_by_pk(pk):

    student = get_one_by_pk(students, pk)

    if student is None:
        return jsonify({}), 404

    return jsonify(student), 200

@app.post("/students/")
def api_add_post():

    # Пример запроса
    # {"full_name": "Василиса", "skills": ["Java", "Spring", "Perl", "Ruby"]}

    # Получаем данные от пользователя из тела запроса
    new_student = request.get_json()
    new_student["pk"] = get_next_pk(students)

    # Добавляем к существующим студентам
    students.append(new_student)

    return jsonify(new_student), 201


if __name__ == '__main__':
    app.run( )
