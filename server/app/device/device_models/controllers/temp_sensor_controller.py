class TempSensorController(object):
    actions = {"Set Server IP": "set_server_ip",
               "Get Temperature": "get_temp"}

    @staticmethod
    def do_action(action, kwargs):
        return getattr(TempSensorController, action)(**kwargs)

    def get_temp():
        return "89"

    def set_server_ip(ip):
        return ip