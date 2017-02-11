from web.extensions import db


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=True)

    def __repr__(self):
        return "Timestamp: {} Message: {}".format(self.message, self.timestamp)
