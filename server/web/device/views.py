from flask import Blueprint, flash, redirect, render_template, request, url_for

from web import database_helper
from web.device_factory import DeviceFactory

blueprint = Blueprint('device', __name__, url_prefix="/device")


@blueprint.route("/<device_id>", methods=["GET", "POST"])
def device_management(device_id):
    device_data = database_helper.get_device_by_id(device_id)
    device_controller = DeviceFactory.factory(device_data.device_type)
    config = device_controller.do_action("get_device_config", device_data)
    if request.method == "POST":
        action = request.form.get("action")
        if action == "remove":
            if database_helper.remove_device_by_id(device_id):
                return redirect(url_for("main.index"))
            else:
                flash("Error! Device was not removed!", "danger")
        elif action == "edit":
            data = request.form.get("data")
            if device_controller.do_action("edit_device_config", device_data, data):
                flash("Updated configuration file sent to device", "success")
                return redirect(url_for(".device_management", device_id=device_id))
            else:
                flash("Error! Something went wrong!", "danger")
        elif action == "device_modify":
            ip = request.form.get("device_ip")
            port = request.form.get("device_port")
            tag = request.form.get("device_tag")
            if database_helper.modify_device_information(device_id, ip, port, tag):
                flash("Updated device information!", "success")
                return redirect(url_for(".device_management", device_id=device_id))
            else:
                flash("Error! Something went wrong!", "danger")
        else:
            value = request.form.get("value")
            if value:
                if device_controller.do_action(action, device_data, value):
                    flash("Success!", "success")
                else:
                    flash("Error: something went wrong!", "danger")
    if device_data.device_type == "MotionSensor":
        notifications = database_helper.get_notifications_for_device(device_id, 10)
    else:
        notifications = None
    context = {
        "device": device_data,
        "config": config,
        "device_controller": device_controller,
        "notifications": notifications
    }
    return render_template("device/device.html", **context)


@blueprint.route("/manage_device/<action>", methods=["POST"])
def manage(action):
    return "yes"
