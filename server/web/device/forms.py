from flask_wtf import Form
from wtforms import HiddenField, SelectField, StringField


class CreateDeviceBindingForm(Form):
    device_id = HiddenField("device_id")
    event_to_monitor = SelectField("Event to Monitor")
    target_device = SelectField("Target Device", coerce=int)
    target_actions = SelectField("Target Device Action", choices=[])
    tag = StringField("Binding Info Tag")

    def __init__(self, device_id, events_to_monitor, target_devices):
        super(CreateDeviceBindingForm, self).__init__()
        self.event_to_monitor.choices = events_to_monitor
        self.target_device.choices = target_devices
        self.device_id.data = device_id
