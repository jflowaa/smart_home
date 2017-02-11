class DeviceFactory(object):
    def factory(device_type):
        if device_type == "MotionSensor":
            return MotionSensor()
        if device_type == "LightBulb":
            return LightBulb()
        if device_type == "TempSensor":
            return TempSensor()
    factory = staticmethod(factory)


class MotionSensor(DeviceFactory):

    @staticmethod
    def get_actions():
        from web.models.controllers import MotionSensorController
        return MotionSensorController.actions

    @staticmethod
    def do_action(action, device, kwargs=None):
        from web.models.controllers import MotionSensorController
        return MotionSensorController.do_action(action, device, kwargs)


class LightBulb(DeviceFactory):

    @staticmethod
    def get_actions():
        from web.models.controllers import LightBulbController
        return LightBulbController.actions

    @staticmethod
    def do_action(action, device, kwargs=None):
        from web.models.controllers import LightBulbController
        return LightBulbController.do_action(action, device, kwargs)


class TempSensor(DeviceFactory):

    @staticmethod
    def get_actions():
        from web.models.controllers import TempSensorController
        return TempSensorController.actions

    @staticmethod
    def do_action(action, device, kwargs=None):
        from web.models.controllers import TempSensorController
        return TempSensorController.do_action(action, device, kwargs)
