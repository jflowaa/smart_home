from flask_wtf import Form
from wtforms import IntegerField, SelectField, StringField, SubmitField


class ChooseDeviceForm(Form):
    device = SelectField("Device", choices=[
        ('LightBulb', 'Light Bulb'),
        ('TempSensor', 'Temperature Sensor'),
        ('MotionSensor', 'Motion Sensor')
    ])


class LightBulbForm(Form):
    tag = StringField('Identifier Name')
    ip = StringField('IP')
    port = IntegerField('Port')
    submit = SubmitField("Add")


class MotionSensorForm(Form):
    tag = StringField('Identifier Name')
    ip = StringField('IP')
    port = IntegerField('Port')
    submit = SubmitField("Add")


class TemperatureDeviceForm(Form):
    tag = StringField('Identifier Name')
    ip = StringField('IP')
    port = IntegerField('Port')
    submit = SubmitField("Add")
