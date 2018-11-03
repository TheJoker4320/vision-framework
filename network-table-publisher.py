import cv2
from IPublish import IPublish
from networktables import NetworkTables

"""Gets Data and sends it to the smart dashboard"""

class NetworkTablePublisher(IPublish):
    table
    def __init__(self,table_name, team_num):
        team = str(team)
        while len(team) != 4:
            team = '0' + team
        ip = '10.'+ team[:2] + '.' + team[2:] + '.2'
        NetworkTables.initialize(ip = server)
        self.table = NetworkTables.getTable(table_name)
    
    def publish(self, data):
        for key in data:
            self.table.putNumber(key, data[key])

