from flask import request
from . import api
from .. import database_helper
from ..device_models import DeviceFactory

@api.route("/motion/<id>", methods=["GET"])
def motion(id):
    database_helper.add_motion_event(id)
    return "200"

@api.route("/device/<id>/action/<action>")
def action(id, action):
    device = database_helper.get_device_by_id(id).__dict__
    device_controller = DeviceFactory.factory(device.get("device_type"))
    device_controller.do_action(action, device)
    return "200"
