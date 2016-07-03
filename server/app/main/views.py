from flask import render_template, url_for, flash, redirect
from . import main
from .. import database_helper
from .validator import Validator
from flask import request
from .forms import ChooseDeviceForm, LightBulbForm, TemperatureDeviceForm, MotionSensorForm


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/adddevice', methods=['POST', 'GET'])
def add_device():
    context = {}
    device_type = "lightbulb"
    if request.method == "POST":
        form = request.form
        error = validate_form(form)
        if not error:
            if database_helper.add_device(form):
                flash("Device Added!", 'success')
                return redirect(url_for(".add_device"))
            else:
                flash("Error! Device was not added!", "danger")
        else:
            context['error'] = error
    if "device" in request.args or request.form.get("device_type"):
        device_type = request.args.get("device") or request.form.get("device_type")
    choose_form, device_form = get_forms(device_type)
    context["device_type"] = device_type
    context["device_form"] = device_form
    context["choose_form"] = choose_form
    return render_template("add_device.html", **context)

@main.route('/removedevice', methods=['POST', 'GET'])
def remove_device():
    context = {}
    device_type = "lightbulb"
    if request.method == "POST":
        device_type = request.form.get("device_type")
        id = request.form.get("id")
        if not database_helper.remove_device(device_type, id):
            flash("Error! Device was not removed!", "danger")
        else:
            flash("Device Removed!", "success")
    if "device" in request.args:
        device_type = request.args.get("device")
    devices = database_helper.get_devices(device_type)
    choose_form, _ = get_forms(device_type)
    context["device_type"] = device_type
    context["choose_form"] = choose_form
    context["devices"] = devices
    return render_template("remove_device.html", **context)


@main.route('/log', methods=["GET"])
def log():
    context = {}
    device_type = "all"
    context["device_type"] = device_type
    return render_template("log.html", **context)

def validate_form(data):
    """
    I don't like this
    """
    validator = Validator()
    for key, value in data.items():
        if key == "tag":
            error = validator.validate_tag(value)
            if error:
                return error
        if key == "ip":
            error = validator.validate_ip(value)
            if error:
                return error
        if key == "port":
            error = validator.validate_port(value)
            if error:
                return error

def get_forms(device_type):
    """
    I don't like this either
    """
    if device_type == "lightbulb":
        device_form = LightBulbForm()
        choose_form = ChooseDeviceForm(device=device_type)
    if device_type == "tempsensor":
        device_form = TemperatureDeviceForm()
        choose_form = ChooseDeviceForm(device=device_type)
    if device_type == "motionsensor":
        device_form = MotionSensorForm()
        choose_form = ChooseDeviceForm(device=device_type)
    return choose_form, device_form
