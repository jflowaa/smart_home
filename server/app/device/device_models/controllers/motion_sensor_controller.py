import socket

class MotionSensorController(object):
    actions = ((True, "Set Server IP", "set_server_ip"),)

    @staticmethod
    def do_action(action, device, kwargs=None):
        if kwargs:
            return getattr(MotionSensorController, action)(device, kwargs)
        else:
            return getattr(MotionSensorController, action)(device)

    def set_server_ip(device, server_ip):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.get("ip"), device.get("port")))
            sock.send(server_ip.encode())
            sock.close()
        except:
            return False
        return True