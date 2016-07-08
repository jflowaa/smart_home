from flask import render_template, url_for, flash, redirect
from .. import database_helper
from . import device
from flask import request
from .device_models import DeviceFactory


@device.route("/<id>", methods=["GET", "POST"])
def device(id):
    context = {}
    context["device"] = database_helper.get_device_by_id(id).__dict__
    context["device_controller"] = create_device(context["device"].get("device_type"))
    context["config"] = context["device_controller"].do_action("get_device_config", context["device"])
    if request.method == "POST":
        action = request.form.get("action")
        if action == "remove":
            if database_helper.remove_device_by_id(id):
                return redirect(url_for("main.index"))
            else:
                flash("Error! Device was not removed!", "danger")
        elif action == "edit":
            data = request.form.get("data")
            if context["device_controller"].do_action("edit_device_config", context["device"], data):
                flash("Updated configuration file sent to device", "success")
                return redirect(url_for(".device", id=id))
            else:
                flash("Error! Something went wrong!", "danger")
        elif action == "device_modify":
            ip = request.form.get("device_ip")
            port = request.form.get("device_port")
            tag = request.form.get("device_tag")
            if database_helper.modify_device_infomation(id, ip, port, tag):
                flash("Updated device infomation!", "success")
                return redirect(url_for(".device", id=id))
            else:
                flash("Error! Something went wrong!", "danger")
        else:
            value = request.form.get("value")
            if value:
                if context["device_controller"].do_action(action, context["device"], value):
                    flash("Success!", "success")
                else:
                    flash("Error: something went wrong!", "danger")
    if context["device"].get("device_type") == "MotionSensor":
        context["notifications"] = database_helper.get_notifications_for_device(id, 10)
    return render_template("device.html", **context)

def create_device(device_type):
    return DeviceFactory.factory(device_type)