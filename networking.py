from networktables import NetworkTables
import time
import json
import collections


def write_initial(name, dic):
    root_table = NetworkTables.getTable(name)

    for item in dic.iteritems():
        __recursive_write(item[0], item[1], root_table)


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
            __recursive_write(sub_item[0], sub_item[1], table.getSubTable(key))


NetworkTables.initialize(server='127.0.0.1')
with open("examples/example.json", "r") as file_handler:
    properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
write_initial("exp", properties)
time.sleep(5)
