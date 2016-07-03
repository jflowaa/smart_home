from . import db

class LightBulb(db.Model):
    __tablename__ = 'LightBulbs'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return "IP: {} Tag: {}".format(self.ip, self.tag)


class MotionSensor(db.Model):
    __tablename__ = 'MotionSensors'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25), nullable=False)
    ip = db.Column(db.String(10), nullable=False)
    port = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "IP: {} Tag: {} Port: {}".format(self.ip, self.tag, self.port)


class TempSensor(db.Model):
    __tablename__ = 'TempSensors'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(25), nullable=False)
    ip = db.Column(db.String(10), nullable=False)
    port = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "IP: {} Tag: {} Port: {}".format(self.ip, self.tag, self.port)
