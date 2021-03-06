import socket


class TempSensorController(object):
    actions = ((False, "Get Temperature", "get_temp"),)

    @staticmethod
    def do_action(action, device, kwargs=None):
        if kwargs:
            return getattr(TempSensorController, action)(device, kwargs)
        else:
            return getattr(TempSensorController, action)(device)

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
