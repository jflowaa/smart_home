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
    if request.method == "POST":
        action = request.form.get("action")
        if action == "remove":
            if database_helper.remove_device_by_id(id):
                flash("Device Removed!", "success")
                return redirect(url_for("main.index"))
            else:
                flash("Error! Device was not removed!", "danger")
    # print(device_controller.list_actions())
    # print(device_controller.do_action("set_server_ip", {"ip": "1"}))
    return render_template("device.html", **context)

def create_device(device_type):
    return DeviceFactory.factory(device_type)