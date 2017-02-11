from web.extensions import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25), nullable=False)
    action = db.Column(db.String(25), nullable=False)
    target_device_id = db.Column(db.Integer, db.ForeignKey("device.id"), nullable=False)
    device = db.relationship("Device", uselist=False)

    def __repr__(self):
        return "ID: {} Tag: {}".format(self.id, self.tag)
