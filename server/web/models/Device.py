from web.extensions import db


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(25), nullable=False)
    tag = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(25), nullable=False)
    port = db.Column(db.Integer)
    notification = db.relationship("Notifications", backref='device')

    def __repr__(self):
        return "IP: {} Tag: {}".format(self.ip, self.tag)
