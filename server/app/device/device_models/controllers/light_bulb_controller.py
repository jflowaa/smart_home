class LightBulbController(object):
    actions = ((False, "Turn On/Off", "turn_on_off"),)

    @staticmethod
    def do_action(action, device):
        return getattr(LightBulbController, action)(**device)

    def turn_on_off():
        return True