from networktables import NetworkTables
import time
import json
import collections


class RemoteTuner(object):
    """
    Responsible for remote tuning of pipeline
    Uses Networktables
    """

    def __init__(self, json_file_name):
        self.json_file_name = json_file_name

        with open(json_file_name, "r") as file_handler:
            pipeline_configurations = json.load(file_handler, object_pairs_hook=collections.OrderedDict)

        sub_table_name = json_file_name.split('/')[-1:][0].replace('.json', '')
        RemoteTuner.__write_initial(sub_table_name, pipeline_configurations)
        self.configurations = pipeline_configurations

    @staticmethod
    def __write_initial(name, dic):
        root_table = NetworkTables.getTable(name)

        for item in dic.iteritems():
            RemoteTuner.__recursive_write(item[0], item[1], root_table)

    @staticmethod
    def __recursive_write(key, value, table):
        """

        :param value:
        :type value: dict
        :param table:
        :type table:
        :return:
        :rtype:
        """
        if type(value) == collections.OrderedDict and len(value) == 0:
            table.getSubTable(key)
        if type(value) != collections.OrderedDict:
            table.putValue(key, value)

        else:
            for sub_item in value.iteritems():
                RemoteTuner.__recursive_write(sub_item[0], sub_item[1], table.getSubTable(key))

    def __listener(self):
        pass


NetworkTables.initialize(server='127.0.0.1')
tuner = RemoteTuner('examples/example.json')
time.sleep(2)
