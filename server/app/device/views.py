from flask import render_template, url_for, flash, redirect
from . import device
from .. import database_helper
from flask import request


@device.route("/<id>", methods=["GET", "POST"])
def device(id):
    context = {}
    if request.method == "POST":
        action = request.form.get("action")
        if action == "remove":
            if database_helper.remove_device_by_id(id):
                flash("Device Removed!", "success")
                return render_template(url_for("main.index"))
            else:
                flash("Error! Device was not removed!", "danger")
    context["device"] = database_helper.get_device_by_id(id).__dict__
    return render_template("device.html", **context)