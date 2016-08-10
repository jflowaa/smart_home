from flask import render_template, url_for, flash, redirect
from . import main
from .. import database_helper
from .validator import Validator
from flask import request
from .forms import ChooseDeviceForm, LightBulbForm, TemperatureDeviceForm, MotionSensorForm
import pygal
from pygal.style import LightColorizedStyle


@main.route('/')
def index():
    notifications = database_helper.get_last_n_notifications(10)
    chart = pygal.Line(x_title="Time", y_title="Temperature (F)", fill=True, interpolate="cubic",
                       style=LightColorizedStyle, print_values=True, disable_xml_declaration=True)
    chart.x_labels = ["12:00PM", "12:30PM", "1:00PM", "1:30PM", "2:00PM", "2:30PM", "3:00PM",
                      "3:30PM", "4:00PM", "4:30PM"]
    tag_name_1_temps = [73, 72, 74, 75, 74, 75, 73, 72, 71, 73]
    tag_name_2_temps = [83, 82, 84, 85, 84, 85, 83, 82, 81, 83]
    chart.add("Tag Name 1", tag_name_1_temps)
    chart.add("Tag Name 2", tag_name_2_temps)
    context = {
        "chart": chart,
        "notifications": notifications
    }
    return render_template("index.html", **context)


@main.route('/devices', methods=["POST", "GET"])
def devices():
    sort_type = "all"
    if request.method == "POST" and request.form.get("sort_type"):
        sort_type = request.form.get("sort_type")
    device_list = database_helper.get_devices(sort_type)
    context = {
        "sort_type": sort_type,
        "devices": device_list,
        "fa_icon": "gear"
    }
    return render_template("devices.html", **context)


@main.route('/adddevice', methods=['POST', 'GET'])
def add_device():
    device_type = "LightBulb"
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
        error = None
    if "device" in request.args or request.form.get("device_type"):
        device_type = request.args.get("device") or request.form.get("device_type")
    choose_form, device_form = get_forms(device_type)
    context = {
        "device_type": device_type,
        "device_form": device_form,
        "choose_form": choose_form,
        "error": error
    }
    return render_template("add_device.html", **context)


@main.route('/removedevice', methods=['POST', 'GET'])
def remove_device():
    device_type = "LightBulb"
    if request.method == "POST":
        device_id = request.form.get("id")
        if not database_helper.remove_device_by_id(device_id):
            flash("Error! Device was not removed!", "danger")
        else:
            flash("Device Removed!", "success")
    if "device" in request.args:
        device_type = request.args.get("device")
    device_list = database_helper.get_devices(device_type)
    choose_form, _ = get_forms(device_type)
    context = {
        "device_type": device_type,
        "fa_icon": "close",
        "choose_form": choose_form,
        "devices": device_list,
    }
    return render_template("remove_device.html", **context)


@main.route('/log', methods=["GET"])
def log():
    device_type = "all"
    device_type = device_type
    notifications = database_helper.get_notifications()
    context = {
        "device_type": device_type,
        "notifications": notifications
    }
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
    if device_type == "LightBulb":
        device_form = LightBulbForm()
        choose_form = ChooseDeviceForm(device=device_type)
    elif device_type == "TempSensor":
        device_form = TemperatureDeviceForm()
        choose_form = ChooseDeviceForm(device=device_type)
    else:
        device_form = MotionSensorForm()
        choose_form = ChooseDeviceForm(device=device_type)
    return choose_form, device_form
