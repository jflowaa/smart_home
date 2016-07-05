class TempSensorController(object):
    actions = ((True, "Set Server IP", "set_server_ip"),
               (False, "Get Temperature", "get_temp"))

    @staticmethod
    def do_action(action, device):
        return getattr(TempSensorController, action)(**device)

    def get_temp():
        return "89"

    def set_server_ip(ip):
        return ip