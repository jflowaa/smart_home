from . import db
from .models import LightBulb, MotionSensor, TempSensor

def add_device(data):
    device_type = data.get("device_type")
    if not device_type:
        return false
    if device_type == "lightbulb":
        return add_lightbulb(data)
    if device_type == "motionsensor":
        return add_motionsensor(data)
    if device_type == "tempsensor":
        return add_tempsensor(data)

def remove_device(device_type, id):
    if not device_type:
        return False
    if device_type == "lightbulb":
        return remove_lightbulb(id)
    if device_type == "motionsensor":
        return remove_motionsensor(id)
    if device_type == "tempsensor":
        return remove_tempsensor(id)


def add_lightbulb(data):
    tag = data.get("tag")
    ip = data.get("ip")
    exists = db.session.query(LightBulb.id).filter_by(ip=ip).scalar() is not None
    if exists:
        return False
    else:
        lightbulb = LightBulb(tag=tag, ip=ip)
        db.session.add(lightbulb)
        db.session.commit()
        return True

def remove_lightbulb(id):
    LightBulb.query.filter(LightBulb.id == int(id)).delete()
    db.session.commit()
    return True

def add_motionsensor(data):
    tag = data.get("tag")
    ip = data.get("ip")
    port = data.get("port")
    exists = db.session.query(MotionSensor.id).filter_by(ip=ip).scalar() is not None
    if exists:
        return False
    else:
        motionsensor = MotionSensor(tag=tag, ip=ip, port=port)
        db.session.add(motionsensor)
        db.session.commit()
        return True

def remove_motionsensor(id):
    MotionSensor.query.filter(MotionSensor.id == int(id)).delete()
    db.session.commit()
    return True

def add_tempsensor(data):
    tag = data.get("tag")
    ip = data.get("ip")
    port = data.get("port")
    exists = db.session.query(TempSensor.id).filter_by(ip=ip).scalar() is not None
    if exists:
        return False
    else:
        tempsensor = TempSensor(tag=tag, ip=ip, port=port)
        db.session.add(tempsensor)
        db.session.commit()
        return True

def remove_tempsensor(id):
    TempSensor.query.filter(TempSensor.id == int(id)).delete()
    db.session.commit()
    return True


def get_devices(device_type):
    if device_type == "lightbulb":
        return get_lightbulbs()
    if device_type == "motionsensor":
        return get_motionsensors()
    if device_type == "tempsensor":
        return get_tempsensors()

def get_lightbulbs():
    return db.session.query(LightBulb).all()

def get_motionsensors():
    return db.session.query(MotionSensor).all()

def get_tempsensors():
    return db.session.query(TempSensor).all()
