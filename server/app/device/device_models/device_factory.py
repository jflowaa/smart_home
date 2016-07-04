class DeviceFactory(object):
    def factory(type):
        if type == "MotionSensor":
            return MotionSensor()
        if type == "LightBulb":
            return LightBulb()
        if type == "TempSensor":
            return TempSensor()
    factory = staticmethod(factory)


class MotionSensor(DeviceFactory):

    def get_actions(self):
        from .controllers import MotionSensorController
        return MotionSensorController.actions

    def do_action(self, action, kwargs):        
        from .controllers import MotionSensorController
        return MotionSensorController.do_action(action, kwargs)

class LightBulb(DeviceFactory):

    def get_actions(self):
        from .controllers import LightBulbController
        return LightBulbController.actions

    def do_action(self, action, kwargs):        
        from .controllers import LightBulbController
        return LightBulbController.do_action(action, kwargs)

class TempSensor(DeviceFactory):

    def get_actions(self):
        from .controllers import TempSensorController
        return TempSensorController.actions

    def do_action(self, action, kwargs):        
        from .controllers import TempSensorController
        return TempSensorController.do_action(action, kwargs)