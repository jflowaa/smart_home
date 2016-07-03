from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, SelectField


class ChooseDeviceForm(Form):
    device = SelectField("Device", choices=[('lightbulb', 'Light Bulb'), ('tempsensor', 'Temperature Sensor'), ('motionsensor', 'Motion Sensor')])

class LightBulbForm(Form):
    tag = StringField('Identifier Name')
    ip = StringField('IP')
    submit = SubmitField("Add Light Bulb")

class MotionSensorForm(Form):
    tag = StringField('Identifier Name')
    ip = StringField('IP')
    port = IntegerField('Port')
    submit = SubmitField("Add Motion Sensor")

class TemperatureDeviceForm(Form):
    tag = StringField('Identifier Name')
    ip = StringField('IP')
    port = IntegerField('Port')
    submit = SubmitField("Add Temperature Device")
