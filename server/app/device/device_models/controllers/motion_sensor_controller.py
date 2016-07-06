import socket

class MotionSensorController(object):
    actions = ()

    @staticmethod
    def do_action(action, device, kwargs=None):
        if kwargs:
            return getattr(MotionSensorController, action)(device, kwargs)
        else:
            return getattr(MotionSensorController, action)(device)

    def get_device_config(device):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((device.get("ip"), device.get("port")))
            msg = "EDIT:"
            sock.send(msg.encode())
            data = sock.recv(1024)
        except:
            return False
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