import socket


class LightBulbController(object):
    actions = ((False, "Turn On/Off", "turn_on_off"),
               (False, "Turn On", "turn_on"))

    @staticmethod
    def do_action(action, device, kwargs=None):
        if kwargs:
            return getattr(LightBulbController, action)(device, kwargs)
        else:
            return getattr(LightBulbController, action)(device)

    @staticmethod
    def get_device_config(device):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.ip, device.port))
            msg = "GET:"
            sock.send(msg.encode())
            data = sock.recv(1024)
        except socket.error:
            return "Unable to connect to device!\nIs the proper script running on the system?"
        return data.decode()

    @staticmethod
    def edit_device_config(device, config):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.ip, device.port))
            msg = "CONFIG:{}".format(config)
            sock.send(msg.encode())
            sock.close()
        except socket.error:
            return False
        return True

    @staticmethod
    def turn_on_off(device):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.ip, device.port))
            msg = "TURNONOFF:"
            sock.send(msg.encode())
        except socket.error:
            return False
        return True

    @staticmethod
    def turn_on(device):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.ip, device.port))
            msg = "TURNON:"
            sock.send(msg.encode())
        except socket.error:
            return False
        return True
