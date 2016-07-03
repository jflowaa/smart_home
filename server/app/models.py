from . import db

class Device(db.Model):
    __tablename__ = 'Devices'
    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(25), nullable=False)
    tag = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(25), nullable=False)
    port = db.Column(db.Integer)

    def __repr__(self):
        return "IP: {} Tag: {}".format(self.ip, self.tag)