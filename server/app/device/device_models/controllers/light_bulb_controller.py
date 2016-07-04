class LightBulbController(object):
    actions = {"Turn On/Off": "turn_on_off"}

    @staticmethod
    def do_action(action, kwargs):
        return getattr(LightBulbController, action)(**kwargs)

    def turn_on_off():
        return True