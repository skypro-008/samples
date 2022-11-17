from flask import Blueprint, render_template
from bp_three.utils import random_int

bp_three = Blueprint("bp_three", __name__, template_folder="templates")


@bp_three.get("/any")
def page_bp_three():
    return render_template("bp_three_index.html")
    # return f"this is page three {random_int()}"
