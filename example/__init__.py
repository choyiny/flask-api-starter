from flask import Blueprint

bp_name = "example"
example_bp = Blueprint(bp_name, __name__, url_prefix="/example")
