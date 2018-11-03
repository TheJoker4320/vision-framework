import cv2
from IPublish import IPublish
from networktables import NetworkTables

"""Gets Data and sends it to the smart dashboard"""

class NetworkTablePublisher(IPublish):
    table
    def __init__(self,table_name):
        NetworkTables.initialize(server= '10.43.20.2')
        self.table = NetworkTables.getTable(table_name)
    
    def publish(self, data):
        for key in data:
            self.table.putNumber(key, data[key])

