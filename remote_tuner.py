from networktables import NetworkTables
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
            self.pipeline_configurations = json.load(file_handler, object_pairs_hook=collections.OrderedDict)

        sub_table_name = json_file_name.split('/')[-1:][0].replace('.json', '')
        self.__write_initial(sub_table_name, self.pipeline_configurations)

    def __write_initial(self, name, dic):
        root_table = NetworkTables.getTable(name)
        for item in dic.iteritems():
            self.__recursive_write(item[0], item[1], root_table)

    def __recursive_write(self, key, value, table):
        """

        :param value:
        :type value: dict
        :param table:
        :type table:
        :return:
        :rtype:
        """

        if type(value) != collections.OrderedDict:
            table.putValue(key, value)

        else:
            if type(value) == list and type(value[0]) == int:
                value = self.__convert_type(value,str)
            sub_table = table.getSubTable(key)
            sub_table.addEntryListener(self.__listener)
            for sub_item in value.iteritems():
                self.__recursive_write(sub_item[0], sub_item[1], sub_table)

    def __convert_type(self,value,type_to):
        strings = []
        for v in value:
            strings.append(type_to(v))
        return strings
    
    def __listener(self, table, key, value, is_new):
        path = table.path
        path_list = path.split('/')[2:]
        current_dictionary = self.pipeline_configurations
        for dictionary_name in path_list:
            current_dictionary = current_dictionary[dictionary_name]
        
        if type(current_dictionary) == list and type(current_dictionary[key] == str):
            current_dictionary[key] = int(current_dictionary[key])

            
        current_dictionary[key] = value
        with open(self.json_file_name, "w") as file_handler:
            json.dump(self.pipeline_configurations, file_handler, indent=0)
