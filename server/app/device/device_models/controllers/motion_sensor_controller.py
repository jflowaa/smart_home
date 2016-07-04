class MotionSensorController(object):
    actions = {"Set Server IP": "set_server_ip"}

    @staticmethod
    def do_action(action, kwargs):
        return getattr(MotionSensorController, action)(**kwargs)

    def set_server_ip(ip):
        return ip