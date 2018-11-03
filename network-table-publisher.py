import cv2
from IPublish import IPublish
from networktables import NetworkTables

"""Gets Data and sends it to the smart dashboard"""

class NetworkTablePublisher(IPublish):
    def __init__(self):
        NetworkTables.initialize(server= '10.43.20.2')
    
    def publish(self, data , table_name):
        table = NetworkTables.getTable(table_name)
        for key in data:
            table.putNumber(key, data[key])

