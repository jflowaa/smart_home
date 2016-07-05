from flask import request
from . import api
from .. import database_helper

@api.route("/motion/<id>", methods=["GET"])
def motion(id):
    database_helper.add_motion_event(id)
    return "200"
