from flask import render_template, url_for, flash, redirect
from . import device
from flask import request


@device.route("/<id>", methods=["GET"])
def device(id):
    return render_template("device.html")