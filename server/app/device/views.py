from flask import render_template, url_for, flash, redirect
from . import device
from .. import database_helper
from flask import request


@device.route("/<id>", methods=["GET"])
def device(id):
    context = {}
    context["device"] = database_helper.get_device_by_id(id).__dict__
    return render_template("device.html", **context)