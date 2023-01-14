from flask import Blueprint
from bp_four.utils import foo

bp_four = Blueprint("bp_four", __name__)


@bp_four.get("/test")
def page_test():
    return "bp_four result" + foo()
