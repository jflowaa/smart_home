from . import db
from .models import Device, Notifications
from datetime import datetime

"""
TODO: Return errors, currently returns true even if error.
"""


def add_device(data):
    device_type = data.get("device_type")
    if not device_type:
        return False
    tag = data.get("tag")
    ip = data.get("ip")
    port = data.get("port") or 0
    device = Device(device_type=device_type, tag=tag, ip=ip, port=port)
    db.session.add(device)
    db.session.commit()
    time = datetime.now()
    notification = Notifications(message="New device added!", timestamp=time, device_id=device.id)
    db.session.add(notification)
    db.session.commit()
    return True


def remove_device_by_id(device_id):
    Device.query.filter(Device.id == int(device_id)).delete()
    db.session.commit()
    time = datetime.now()
    notification = Notifications(message="Device removed!", timestamp=time, device_id=None)
    db.session.add(notification)
    db.session.query(Notifications).filter(Notifications.device_id == device_id).first().device_id = None
    db.session.commit()
    return True


def get_notifications():
    return db.session.query(Notifications).order_by(Notifications.id.desc()).all()


def get_last_n_notifications(n):
    return db.session.query(Notifications).order_by(Notifications.id.desc()).limit(n).all()


def get_notifications_for_device(device_id, n):
    return db.session.query(Notifications).filter(Notifications.device_id == device_id)\
        .order_by(Notifications.id.desc()).limit(n).all()


def get_devices(device_type):
    if device_type == "all":
        return get_all_devices()
    else:
        return get_type_devices(device_type)


def get_device_by_id(device_id):
    return db.session.query(Device).get(device_id)


def get_all_devices():
    return db.session.query(Device).all()


def get_type_devices(device_type):
    return db.session.query(Device).filter(Device.device_type == device_type).all()


def modify_device_information(device_id, ip, port, tag):
    device = db.session.query(Device).filter(Device.id == device_id).first()
    device.ip = ip
    device.port = port
    device.tag = tag
    db.session.commit()
    return True


def add_motion_event(device_id):
    time = datetime.now()
    notification = Notifications(message="Motion Detected", timestamp=time, device_id=device_id)
    db.session.add(notification)
    db.session.commit()
    return True
