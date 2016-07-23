import socket


class LightBulbController(object):
    actions = ((False, "Turn On/Off", "turn_on_off"),)

    @staticmethod
    def do_action(action, device, kwargs=None):
        if kwargs:
            return getattr(LightBulbController, action)(device, kwargs)
        else:
            return getattr(LightBulbController, action)(device)

    def get_device_config(device):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.get("ip"), device.get("port")))
            msg = "GET:"
            sock.send(msg.encode())
            data = sock.recv(1024)
        except:
            return "Unable to connect to device!\nIs the proper script running on the system?"
        return data.decode()

    def edit_device_config(device, config):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.get("ip"), device.get("port")))
            msg = "CONFIG:{}".format(config)
            sock.send(msg.encode())
            sock.close()
        except:
            return False
        return True

    def turn_on_off(device):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.get("ip"), device.get("port")))
            msg = "TURNONOFF:"
            sock.send(msg.encode())
        except:
            False
        return True