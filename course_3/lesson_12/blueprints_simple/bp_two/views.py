from flask import Blueprint

bp_two = Blueprint("bp_two", __name__)

@bp_two.get("/")
def page_index():
    return "Я страничка блюпринта two"
