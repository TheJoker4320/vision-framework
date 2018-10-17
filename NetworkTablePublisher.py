import cv2
from IPublish import IPublish
from networktables import NetworkTables


class NetworkTablePublisher(IPublish):
    def __init__(self):
        pass

    """Gets Data and sends it to the smart dashboard"""
    def publish(self, data):
        table = NetworkTables.getTable('SmartDashboard')
        for key in data:
            table.putNumber(key, data[key])
            print 'sended', data[key]


