from publish import Publish
from networktables import NetworkTables


class NetworkTablePublisher(Publish):
    """
    Gets Data ,team number and table name.
    Sends it to the specified table via network tables protocol.
    """
    ip_template = "10.(0).(1).2"

    def __init__(self, table_name, team_num):
        team_num = '0' * (4 - len(str(team_num))) + str(team_num)
        ip = NetworkTablePublisher.ip_template.format(team_num[:2], team_num[2:])
        NetworkTables.initialize(ip)
        self.table = NetworkTables.getTable(table_name)

    def publish(self, data):
        print data
        for key, value in data.iteritems():
            self.table.putValue(key, value)
