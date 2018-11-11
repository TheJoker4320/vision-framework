from IPublish import IPublish
from networktables import NetworkTables


class NetworkTablePublisher(IPublish):
    """
    Gets Data ,team number and table name sends it to the specified
    table via network tables protocol
    """
    def __init__(self, table_name, team_num):
        team = str(team_num)
        while len(team) != 4:
            team = '0' + team
        ip = '10.' + team[:2] + '.' + team[2:] + '.2'
        NetworkTables.initialize(ip)
        self.table = NetworkTables.getTable(table_name)

    def publish(self, data):
        for key in data:
            self.table.putNumber(key, data[key])
