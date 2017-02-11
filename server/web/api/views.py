# -*- coding: utf-8 -*-
"""API section, device communication"""
from flask import Blueprint, jsonify

from web.device_factory import DeviceFactory

from .. import database_helper

blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.route("/motion/<device_id>")
def motion(device_id):
    database_helper.add_motion_event(device_id)
    return jsonify({"success": True})


@blueprint.route("/device/<device_id>/action/<device_action>")
def action(device_id, device_action):
    device = database_helper.get_device_by_id(device_id)
    device_controller = DeviceFactory.factory(device.device_type)
    device_controller.do_action(device_action, device)
    return jsonify({"success": True})


@blueprint.route("/device/notifications", methods=["POST"])
def device_notifications():
    notifications = database_helper.get_last_n_notifications()
    data = []
    for notification in notifications:
        d = {
            "id": notification.id,
            "device_id": notification.device_id,
            "message": notification.message,
            "timestamp": notification.timestamp.strftime("%y-%b-%d %I:%M%p")
        }
        data.append(d)
    return jsonify({"success": True, "data": data})
