from . import db
from .models import Device

def add_device(data):
    device_type = data.get("device_type")
    if not device_type:
        return false
    tag = data.get("tag")
    ip = data.get("ip")
    port = data.get("port") or 0
    device = Device(device_type=device_type, tag=tag, ip=ip, port=port)
    db.session.add(device)
    db.session.commit()
    return True

def remove_device_by_id(id):
    Device.query.filter(Device.id == int(id)).delete()
    db.session.commit()
    return True

def get_devices(device_type):
    if device_type == "all":
        return get_all_devices()
    else:
        return get_type_devices(device_type)

def get_device_by_id(id):
    return db.session.query(Device).get(id)

def get_all_devices():
    return db.session.query(Device).all()

def get_type_devices(device_type):
    return db.session.query(Device).filter(Device.device_type == device_type).all()
