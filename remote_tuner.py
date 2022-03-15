from networktables import NetworkTables
import json
import collections
from pipeline.pipeline_factory import PipelineFactory


class RemoteTuner(object):
    """
    Responsible for remote tuning of the pipeline
    """

    def __init__(self, json_file_name, pipeline):
        self.json_file_name = json_file_name

        with open(json_file_name, "r") as file_handler:
            self.pipeline_configurations = json.load(file_handler, object_pairs_hook=collections.OrderedDict)

        sub_table_name = json_file_name.split('/')[-1:][0].replace('.json', '')
        self.__write_initial(sub_table_name, self.pipeline_configurations)
        self.pipeline = pipeline

    def __write_initial(self, name, dic):
        root_table = NetworkTables.getTable(name)
        for item in dic.items():
            self.__recursive_write(item[0], item[1], root_table)

    def __recursive_write(self, key, value, table):
        """
        Puts a specific value in a specific place (key)
        recursively into the desired table
        """

        if type(value) != collections.OrderedDict:
            if type(value) == list and (type(value[0]) == float or type(value[0]) == int):
                value = [str(num) for num in value]
            table.putValue(key, value)

        else:
            print("________________________________", value, "___________________________________")
            sub_table = table.getSubTable(key)
            sub_table.addEntryListener(self.__listener)
            for sub_item in value.items():
                self.__recursive_write(sub_item[0], sub_item[1], sub_table)

    def __listener(self, table, key, value, is_new):
        print("hello __ my old friend")
        path = table.path
        path_list = path.split('/')[2:]
        current_dictionary = self.pipeline_configurations
        for dictionary_name in path_list:
            current_dictionary = current_dictionary[dictionary_name]
        if type(value) == tuple and type(value[0]) == str:
            if "." in value[0]:
                current_dictionary[key] = [float(num) for num in value]
            else:
                current_dictionary[key] = [int(num) for num in value]
        else:
            current_dictionary[key] = value
        with open(self.json_file_name, "w") as file_handler:
            json.dump(self.pipeline_configurations, file_handler, indent=0)
        self.pipeline = PipelineFactory.create_pipeline(self.pipeline_configurations)

    def get_pipeline(self):
        return self.pipeline
