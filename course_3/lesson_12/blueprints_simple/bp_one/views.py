from flask import Blueprint

bp_one = Blueprint("bp_one", __name__)


@bp_one.get("/")
def page_index():
    return "Я страничка блюпринта one"
