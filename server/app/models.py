from . import db

class Device(db.Model):
    __tablename__ = 'Devices'
    id = db.Column(db.Integer, primary_key=True)
    notification = db.relationship("Notification", backref='Notifications')
    device_type = db.Column(db.String(25), nullable=False)
    tag = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(25), nullable=False)
    port = db.Column(db.Integer)

    def __repr__(self):
        return "IP: {} Tag: {}".format(self.ip, self.tag)


class Notification(db.Model):
    __tablename__ = "Notifications"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('Devices.id'))
    message = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return "Device ID: {} Timestamp: {} Message: {}".format(device_id, message, timestamp)
