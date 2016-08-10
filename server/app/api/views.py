from . import api
from .. import database_helper
from ..device_models import DeviceFactory


@api.route("/motion/<device_id>", methods=["GET"])
def motion(device_id):
    database_helper.add_motion_event(device_id)
    return "200"


@api.route("/device/<device_id>/action/<device_action>")
def action(device_id, device_action):
    device = database_helper.get_device_by_id(device_id).__dict__
    device_controller = DeviceFactory.factory(device.get("device_type"))
    device_controller.do_action(device_action, device)
    return "200"
